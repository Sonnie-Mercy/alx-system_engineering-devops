#!/usr/bin/env ruby
log_file = ARGV[0]
log_data = File.read(log_file)
pattern = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/
matches = log_data.scan(pattern)
matches.each do |match|
  sender = match[0]
  receiver = match[1]
  flags = match[2]
  puts "#{sender},#{receiver},#{flags}"
end

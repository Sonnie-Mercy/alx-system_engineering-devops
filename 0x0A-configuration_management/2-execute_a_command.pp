# A puppet manifest that kills a process called killmenow
exec { 'kill_killmenow_process':
  command => 'pkill killmenow',
  onlyif  => 'pgrep killmenow',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
  require => Package['procps'],  # Make sure the 'procps' package is installed
}

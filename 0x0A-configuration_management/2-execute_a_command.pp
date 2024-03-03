# kill a process

exec { 'kill_me_now':
command   => 'pkill -f killmenow',
path      => '/usr/bin',
logoutput =>  true,
provider  => 'shell',
}

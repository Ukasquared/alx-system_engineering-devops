# kill a process

exec { 'kill_me_now':
command     => 'pkill -f killmenow',
refreshonly =>  true,
logoutput   =>  true,
}

# Creates a file
file { '/tmp/school':
  mode    => '0744',
  content => 'I love Puppet',
  path    => '/tmp/school',
  ensure  => file,
  owner   => 'www-data',
  group   => 'www-data'
}

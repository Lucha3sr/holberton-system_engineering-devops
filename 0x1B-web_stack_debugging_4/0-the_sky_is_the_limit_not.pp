#fix Nginx requests failed
exec { 'limit_requests_increase':
command => 'sed -i "s/15/4096/g" /etc/default/nginx; sudo service nginx restart',
path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin']
}

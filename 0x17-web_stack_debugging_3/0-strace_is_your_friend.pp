# fix wordpress 500 error
exec { 'replace_line':
  command => 'sed -i s/phpp/php /var/www/html/wp-settings.php; sudo service apache2 restart',
}
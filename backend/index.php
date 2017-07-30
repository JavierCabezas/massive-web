<?php
/**
 * Created by PhpStorm.
 * User: javier
 * Date: 7/30/17
 * Time: 1:00 PM
 */
$loc = 'Location: ' . "http://$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]"."web";
header($loc);
die();


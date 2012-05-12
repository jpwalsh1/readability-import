readability-import
==================

Import Readability Bookmarks into a local database

Structure for the database

    CREATE TABLE IF NOT EXISTS `bookmarks` (
      `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
      `bid` int(10) unsigned NOT NULL,
      `title` text NOT NULL,
      `url` varchar(2083) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

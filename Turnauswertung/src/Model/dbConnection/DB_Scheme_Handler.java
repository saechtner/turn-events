package Model.dbConnection;

public class DB_Scheme_Handler {
//
//    SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
//
///*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
///*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
///*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
///*!40101 SET NAMES utf8 */;
//
//    DROP TABLE IF EXISTS 'Wertung';
//    DROP TABLE IF EXISTS 'Sportler';
//    DROP TABLE IF EXISTS 'Mannschaft';
//    DROP TABLE IF EXISTS 'Wertungsgruppe';
//    DROP TABLE IF EXISTS 'Finale';
//    DROP TABLE IF EXISTS 'Sportart';
//    DROP TABLE IF EXISTS 'Riege';
//    DROP TABLE IF EXISTS 'Verein';
//
//
//
//    CREATE TABLE IF NOT EXISTS 'Finale' (
//            'FinaleID' INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
//    'FinaleAnzTeilnehmer' int(3) NOT NULL,
//    'WettkampfID' INT NOT NULL,
//    FOREIGN KEY ('WettkampfID') REFERENCES 'Wettkampf' ('WettkampfID')
//            ) ENGINE=InnoDB  DEFAULT CHARSET=latin1;
//
//    CREATE TABLE IF NOT EXISTS 'Wertungsgruppe' (
//            'WertungsgruppeID' INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
//    'WertungsgruppeName' VARCHAR(100) NOT NULL,
//    'WertungsgruppeAnzahlZuWerten' INT NOT NULL, # is inf for Einzel
//    'WettkampfID' INT NOT NULL,
//    FOREIGN KEY ('WettkampfID') REFERENCES 'Wettkampf' ('WettkampfID')
//            ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
//
//    CREATE TABLE IF NOT EXISTS 'Mannschaft' (
//            'MannschaftID' INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
//    'MannschaftName' VARCHAR(100),
//    'WettkampfID' INT NOT NULL,
//            'WertungsgruppeID' INT NOT NULL,
//    FOREIGN KEY ('WertungsgruppeID') REFERENCES 'Wertungsgruppe' ('WertungsgruppeID'),
//    FOREIGN KEY ('WettkampfID') REFERENCES 'Wettkampf' ('WettkampfID')
//            ) ENGINE=InnoDB  DEFAULT CHARSET=latin1;
//
//    CREATE TABLE IF NOT EXISTS 'Sportler' (
//            'SportlerID' INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
//    'SportlerNachname' VARCHAR(100) NOT NULL,
//    'SportlerVorname' VARCHAR(100) NOT NULL,
//    'SportlerGeschlecht' VARCHAR(1) NOT NULL,
//    'SportlerGeburtsjahr' SMALLINT,
//            'WettkampfID' INT NOT NULL,
//            'WertungsgruppeID' INT NOT NULL,
//            'RiegeID' INT,
//            'MannschaftID' INT,
//    FOREIGN KEY ('WettkampfID') REFERENCES 'Wettkampf' ('WettkampfID'),
//    FOREIGN KEY ('RiegeID') REFERENCES 'Riege' ('RiegeID'),
//    FOREIGN KEY ('WertungsgruppeID') REFERENCES 'Wertungsgruppe' ('WertungsgruppeID'),
//    FOREIGN KEY ('MannschaftID') REFERENCES 'Mannschaft' ('MannschaftID')
//            ) ENGINE=InnoDB  DEFAULT CHARSET=latin1;
//
//    CREATE TABLE IF NOT EXISTS 'Wertung' (
//            'WettkampfID' INT NOT NULL,
//            'SportlerID' INT NOT NULL,
//            'SportartID' INT NOT NULL,
//            'Ergebnis' DOUBLE NOT NULL,
//    PRIMARY KEY ('WettkampfID', 'SportlerID', 'SportartID'),
//    FOREIGN KEY ('WettkampfID') REFERENCES 'Wettkampf' ('WettkampfID'),
//    FOREIGN KEY ('SportlerID') REFERENCES 'Sportler' ('SportlerID'),
//    FOREIGN KEY ('SportartID') REFERENCES 'Sportart' ('SportartID')
//            ) ENGINE=InnoDB  DEFAULT CHARSET=latin1;

    static String createWettkampf(){
        return "CREATE TABLE IF NOT EXISTS 'Wettkampf' (" +
                "'WettkampfID' INT PRIMARY KEY NOT NULL AUTO_INCREMENT," +
                "'WettkampfName' VARCHAR(100) NOT NULL" +
               ") ENGINE=InnoDB  DEFAULT CHARSET=latin1;";
    }

    static String dropWettkampf(){
        return "DROP TABLE IF EXISTS 'Wettkampf';";
    }

    static String createVerein(){
        return "CREATE TABLE IF NOT EXISTS 'Verein' (" +
                "'VereinID' INT PRIMARY KEY NOT NULL AUTO_INCREMENT," +
                "'VereinName' VARCHAR(100) NOT NULL" +
                ") ENGINE=InnoDB  DEFAULT CHARSET=latin1;";
    }

    static String createRiege(){
        return "CREATE TABLE IF NOT EXISTS 'Riege' (" +
                "'RiegeID' INT PRIMARY KEY NOT NULL AUTO_INCREMENT" +
                ") ENGINE=InnoDB  DEFAULT CHARSET=latin1;";
    }

    static String createSportart(){
        return "CREATE TABLE IF NOT EXISTS 'Sportart' (" +
                "'SportartID' INT PRIMARY KEY NOT NULL AUTO_INCREMENT," +
                "'SportartName' VARCHAR(100) NOT NULL" +
                ") ENGINE=InnoDB DEFAULT CHARSET=latin1;";
    }

    static String createFinale(){
        return "CREATE TABLE IF NOT EXISTS 'Verein' (" +
                "'VereinID' INT PRIMARY KEY NOT NULL AUTO_INCREMENT," +
                "'VereinName' VARCHAR(100) NOT NULL" +
                ") ENGINE=InnoDB  DEFAULT CHARSET=latin1;";
    }

    static String createWertungsgruppe(){
        return "CREATE TABLE IF NOT EXISTS 'Verein' (" +
                "'VereinID' INT PRIMARY KEY NOT NULL AUTO_INCREMENT," +
                "'VereinName' VARCHAR(100) NOT NULL" +
                ") ENGINE=InnoDB  DEFAULT CHARSET=latin1;";
    }

    static String createMannschaft(){
        return "CREATE TABLE IF NOT EXISTS 'Verein' (" +
                "'VereinID' INT PRIMARY KEY NOT NULL AUTO_INCREMENT," +
                "'VereinName' VARCHAR(100) NOT NULL" +
                ") ENGINE=InnoDB  DEFAULT CHARSET=latin1;";
    }

    static String createSportler(){
        return "CREATE TABLE IF NOT EXISTS 'Verein' (" +
                "'VereinID' INT PRIMARY KEY NOT NULL AUTO_INCREMENT," +
                "'VereinName' VARCHAR(100) NOT NULL" +
                ") ENGINE=InnoDB  DEFAULT CHARSET=latin1;";
    }

    static String createWertung(){
        return "CREATE TABLE IF NOT EXISTS 'Verein' (" +
                "'VereinID' INT PRIMARY KEY NOT NULL AUTO_INCREMENT," +
                "'VereinName' VARCHAR(100) NOT NULL" +
                ") ENGINE=InnoDB  DEFAULT CHARSET=latin1;";
    }

    static String createWertungsgruppeMisstInSportart(){
        return "CREATE TABLE IF NOT EXISTS 'WertungsgruppeMisstInSportart' (" +
                "'SportartID' INT NOT NULL," +
                "'WertungsgruppeID' INT NOT NULL" +
                ") ENGINE=InnoDB  DEFAULT CHARSET=latin1;";
    }


}

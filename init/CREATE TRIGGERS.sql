-- perles
CREATE OR REPLACE FUNCTION process_perles_audit() RETURNS TRIGGER AS 
$perles_audit$
    BEGIN
               IF (TG_OP = 'DELETE') THEN
            INSERT INTO perles_audit SELECT 'D', now(), user, OLD.*;
            RETURN OLD;
        ELSIF (TG_OP = 'UPDATE') THEN
            INSERT INTO perles_audit SELECT 'U', now(), user, NEW.*;
            RETURN NEW;
        ELSIF (TG_OP = 'INSERT') THEN
            INSERT INTO perles_audit SELECT 'I', now(), user, NEW.*;
            RETURN NEW;
        END IF;
        RETURN NULL; -- result is ignored since this is an AFTER trigger
    END;
$perles_audit$ LANGUAGE plpgsql;

CREATE TRIGGER perles_audit
AFTER INSERT OR UPDATE OR DELETE ON perles
    FOR EACH ROW EXECUTE PROCEDURE process_perles_audit();


-- colliers
CREATE OR REPLACE FUNCTION process_colliers_audit() RETURNS TRIGGER AS 
$colliers_audit$
    BEGIN
        IF (TG_OP = 'DELETE') THEN
            INSERT INTO colliers_audit SELECT 'D', now(), user, OLD.*;
            RETURN OLD;
        ELSIF (TG_OP = 'UPDATE') THEN
            INSERT INTO colliers_audit SELECT 'U', now(), user, NEW.*;
            RETURN NEW;
        ELSIF (TG_OP = 'INSERT') THEN
            INSERT INTO colliers_audit SELECT 'I', now(), user, NEW.*;
            RETURN NEW;
        END IF;
        RETURN NULL; -- result is ignored since this is an AFTER trigger
    END;
$colliers_audit$ LANGUAGE plpgsql;

CREATE TRIGGER colliers_audit
AFTER INSERT OR UPDATE OR DELETE ON colliers
    FOR EACH ROW EXECUTE PROCEDURE process_colliers_audit();

-- chaines
CREATE OR REPLACE FUNCTION process_chaines_audit() RETURNS TRIGGER AS 
$chaines_audit$
    BEGIN
        IF (TG_OP = 'DELETE') THEN
            INSERT INTO chaines_audit SELECT 'D', now(), user, OLD.*;
            RETURN OLD;
        ELSIF (TG_OP = 'UPDATE') THEN
            INSERT INTO chaines_audit SELECT 'U', now(), user, NEW.*;
            RETURN NEW;
        ELSIF (TG_OP = 'INSERT') THEN
            INSERT INTO chaines_audit SELECT 'I', now(), user, NEW.*;
            RETURN NEW;
        END IF;
        RETURN NULL; -- result is ignored since this is an AFTER trigger
    END;
$chaines_audit$ LANGUAGE plpgsql;

CREATE TRIGGER chaines_audit
AFTER INSERT OR UPDATE OR DELETE ON chaines
    FOR EACH ROW EXECUTE PROCEDURE process_chaines_audit();

-- pendentifs
CREATE OR REPLACE FUNCTION process_pendentifs_audit() RETURNS TRIGGER AS 
$pendentifs_audit$
    BEGIN
        IF (TG_OP = 'DELETE') THEN
            INSERT INTO pendentifs_audit SELECT 'D', now(), user, OLD.*;
            RETURN OLD;
        ELSIF (TG_OP = 'UPDATE') THEN
            INSERT INTO pendentifs_audit SELECT 'U', now(), user, NEW.*;
            RETURN NEW;
        ELSIF (TG_OP = 'INSERT') THEN
            INSERT INTO pendentifs_audit SELECT 'I', now(), user, NEW.*;
            RETURN NEW;
        END IF;
        RETURN NULL; -- result is ignored since this is an AFTER trigger
    END;
$pendentifs_audit$ LANGUAGE plpgsql;

CREATE TRIGGER pendentifs_audit
AFTER INSERT OR UPDATE OR DELETE ON pendentifs
    FOR EACH ROW EXECUTE PROCEDURE process_pendentifs_audit();

-- transactions_locales
CREATE OR REPLACE FUNCTION process_transactions_locales_audit() RETURNS TRIGGER AS 
$transactions_locales_audit$
    BEGIN
        IF (TG_OP = 'DELETE') THEN
            INSERT INTO transactions_locales_audit SELECT 'D', now(), user, OLD.*;
            RETURN OLD;
        ELSIF (TG_OP = 'UPDATE') THEN
            INSERT INTO transactions_locales_audit SELECT 'U', now(), user, NEW.*;
            RETURN NEW;
        ELSIF (TG_OP = 'INSERT') THEN
            INSERT INTO transactions_locales_audit SELECT 'I', now(), user, NEW.*;
            RETURN NEW;
        END IF;
        RETURN NULL; -- result is ignored since this is an AFTER trigger
    END;
$transactions_locales_audit$ LANGUAGE plpgsql;

CREATE TRIGGER transactions_locales_audit
AFTER INSERT OR UPDATE OR DELETE ON transactions_locales
FOR EACH ROW EXECUTE PROCEDURE process_transactions_locales_audit();

-- clients
CREATE OR REPLACE FUNCTION process_clients_audit() RETURNS TRIGGER AS 
$clients_audit$
    BEGIN
        IF (TG_OP = 'DELETE') THEN
            INSERT INTO clients_audit SELECT 'D', now(), user, OLD.*;
            RETURN OLD;
        ELSIF (TG_OP = 'UPDATE') THEN
            INSERT INTO clients_audit SELECT 'U', now(), user, NEW.*;
            RETURN NEW;
        ELSIF (TG_OP = 'INSERT') THEN
            INSERT INTO clients_audit SELECT 'I', now(), user, NEW.*;
            RETURN NEW;
        END IF;
        RETURN NULL; -- result is ignored since this is an AFTER trigger
    END;
$clients_audit$ LANGUAGE plpgsql;

CREATE TRIGGER clients_audit
AFTER INSERT OR UPDATE OR DELETE ON clients
FOR EACH ROW EXECUTE PROCEDURE process_clients_audit();

-- cartes
CREATE OR REPLACE FUNCTION process_cartes_audit() RETURNS TRIGGER AS 
$cartes_audit$
    BEGIN
        IF (TG_OP = 'DELETE') THEN
            INSERT INTO cartes_audit SELECT 'D', now(), user, OLD.*;
            RETURN OLD;
        ELSIF (TG_OP = 'UPDATE') THEN
            INSERT INTO cartes_audit SELECT 'U', now(), user, NEW.*;
            RETURN NEW;
        ELSIF (TG_OP = 'INSERT') THEN
            INSERT INTO cartes_audit SELECT 'I', now(), user, NEW.*;
            RETURN NEW;
        END IF;
        RETURN NULL; -- result is ignored since this is an AFTER trigger
    END;
$cartes_audit$ LANGUAGE plpgsql;

CREATE TRIGGER cartes_audit
AFTER INSERT OR UPDATE OR DELETE ON cartes
FOR EACH ROW EXECUTE PROCEDURE process_cartes_audit();
-- upgrade --
CREATE TABLE IF NOT EXISTS "records" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "full_name" VARCHAR(50),
    "val_1" BOOL NOT NULL  DEFAULT False,
    "val_2" BOOL NOT NULL  DEFAULT False,
    "val_3" BOOL NOT NULL  DEFAULT False,
    "val_4" BOOL NOT NULL  DEFAULT False,
    "val_5" BOOL NOT NULL  DEFAULT False
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);

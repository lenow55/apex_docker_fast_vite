-- upgrade --
CREATE TABLE IF NOT EXISTS "records" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "blocked_acess" INT NOT NULL  DEFAULT 0,
    "age_limit" INT NOT NULL,
    "theam_restriction" INT NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);

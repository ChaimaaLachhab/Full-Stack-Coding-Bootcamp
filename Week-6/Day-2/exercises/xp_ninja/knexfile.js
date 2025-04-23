module.exports = {
    development: {
      client: 'pg',
      connection: {
        host: 'localhost',
        port: '5432',
        user: 'postgres',
        password: '1234',
        database: 'users'
      },
      migrations: {
        directory: './server/config/migrations'
      },
      seeds: {
        directory: './server/config/seeds'
      }
    }
  };
  
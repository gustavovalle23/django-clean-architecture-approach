import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { ClientsModule, Transport } from '@nestjs/microservices';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import configuration from './env';

@Module({
  imports: [
    ConfigModule.forRoot({
      isGlobal: true,
      load: [configuration],
    }),
    ClientsModule.register([
      {
        name: 'BOOK_SERVICE',
        transport: Transport.KAFKA,
        options: {
          client: {
            clientId: 'book-app',
            brokers: ['kafka:9092'],
          },
          consumer: {
            groupId: 'book-app-consumer',
          },
        },
      },
    ]),
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}

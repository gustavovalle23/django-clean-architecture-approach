import { ConfigService } from '@nestjs/config';
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { kafkaConfig } from './configs';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  const configService = app.get<ConfigService>(ConfigService);
  app.connectMicroservice(kafkaConfig(configService));
  await app.startAllMicroservices();
  await app.listen(3000);
}
bootstrap();

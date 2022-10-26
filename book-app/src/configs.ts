import { ConfigService } from '@nestjs/config';
import { MicroserviceOptions, Transport } from '@nestjs/microservices';

export const kafkaConfig = (
  configService: ConfigService,
): MicroserviceOptions => {
  return {
    transport: Transport.KAFKA,
    options: {
      client: {
        clientId: configService.get<string>('kafka.clientId'),
        brokers: configService.get<string[]>('kafka.brokers'),
      },
      consumer: {
        groupId: configService.get<string>('kafka.groupId'),
      },
    },
  };
};

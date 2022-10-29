import { Controller, Get } from '@nestjs/common';
import { EventPattern, Payload } from '@nestjs/microservices';
import { debug } from 'console';
import { AppService } from './app.service';

class FinishBookMessage {
  name: string;
  days: number;
}

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  async getHello(): Promise<string> {
    const message = this.appService.getHello();
    const encodedMessage = await this.appService.encodeMessage(message);
    debug('Encoded message: ', encodedMessage);
    return message;
  }

  @EventPattern('finish.book')
  finishBook(@Payload() { name, days }: FinishBookMessage): any {
    debug(`Finish the book ${name} in ${days} days`);
  }
}

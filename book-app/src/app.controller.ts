import { Controller, Get } from '@nestjs/common';
import { EventPattern, Payload } from '@nestjs/microservices';
import { debug } from 'console';
import { AppService } from './app.service';

class FinishBookMessage {
  bookName: string;
  days: number;
}

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  getHello(): string {
    return this.appService.getHello();
  }

  @EventPattern('finish.book')
  finishBook(@Payload() { bookName, days }: FinishBookMessage): any {
    debug(`Finish the book ${bookName} in ${days} days`);
  }
}

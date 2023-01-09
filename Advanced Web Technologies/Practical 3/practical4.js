// Mayur Jivani - 20BCP311D //
import { EventEmitter } from 'node:events';
class MyEmitter extends EventEmitter {}

const myEmitter = new MyEmitter();
myEmitter.on('WaterFull', function(a, b) {
    console.log(`Turned off ${a} no ${b} successfully!`)
});
myEmitter.emit('WaterFull', 'Switch', '21');
/*
 * delay.c
 *
 *  Created on: Apr 3, 2023
 *      Author: lanza
 */
#include "delay.h"

  delay_t a;
  void delayInit(delay_t * delay, tick_t duration){
	  delay-> duration = duration;
	  delay -> running = false;
  }

  bool_t delayRead( delay_t * delay ) {
  	if(!delay->running) {
  		delay->startTime = HAL_GetTick();
  		delay->running = true;
  	}
  	else if(HAL_GetTick() - delay->startTime >= delay->duration) {
  		delay->running = false;
  		return true;
  	}
  	return false;
  }


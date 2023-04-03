################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (10.3-2021.10)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Drivers/delays/delay.c 

OBJS += \
./Drivers/delays/delay.o 

C_DEPS += \
./Drivers/delays/delay.d 


# Each subdirectory must supply rules for building sources it contributes
Drivers/delays/%.o Drivers/delays/%.su Drivers/delays/%.cyclo: ../Drivers/delays/%.c Drivers/delays/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m7 -std=gnu11 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32F767xx -c -I../Core/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32F7xx/Include -I../Drivers/CMSIS/Include -I"D:/STM32_GITHUB/clase/Drivers/BSP" -I"D:/STM32_GITHUB/clase/Drivers/delays" -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -fcyclomatic-complexity -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv5-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-Drivers-2f-delays

clean-Drivers-2f-delays:
	-$(RM) ./Drivers/delays/delay.cyclo ./Drivers/delays/delay.d ./Drivers/delays/delay.o ./Drivers/delays/delay.su

.PHONY: clean-Drivers-2f-delays


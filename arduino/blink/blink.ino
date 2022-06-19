void setup() {
    // Change pin mode (pin_nmb, mode)
    pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
    // Change pin status to high
    digitalWrite(LED_BUILTIN, HIGH);
    // Wait 1000 mili seconds
    delay(1000);
    digitalWrite(LED_BUILTIN, LOW);
    delay(1000);
}
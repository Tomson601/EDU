void setup() {
  // 4A bits:
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  // Set bit to 0 [LOW]:
  digitalWrite(2, LOW);
  digitalWrite(3, LOW);
  digitalWrite(4, LOW);
  digitalWrite(5, LOW);

  // 4B bits:
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  // Set bit to 0 [LOW]:
  digitalWrite(8, LOW);
  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
  digitalWrite(11, LOW);

}

void loop() {
  // 1+1:
  digitalWrite(2, HIGH);
  digitalWrite(3, HIGH);
  digitalWrite(4, HIGH);
//  digitalWrite(5, HIGH);
  digitalWrite(8, HIGH);
//  digitalWrite(9, HIGH);
//  digitalWrite(10, HIGH);
//  digitalWrite(11, HIGH);
  delay(2500);
}

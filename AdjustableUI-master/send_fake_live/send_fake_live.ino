void setup() {
  Serial.begin(9600);

}

void loop() {
  String a = String(float(random(1, 1000)/1000.0));
  String b = String(float(random(1, 1000)/1000.0));
  String c = String(float(random(1, 1000)/1000.0));
  String d = String(float(random(1, 1000)/1000.0));
  String e = String(float(random(1, 1000)/1000.0));

  Serial.println(a + ',' + b + ',' + c + ',' + d + ',' + e);
}

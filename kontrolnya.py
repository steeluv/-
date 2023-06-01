"""4.	Класс «ПчёлоСлон» (BeeElephant) Экземпляр класса инициализируется двумя целыми числами:
первое относится к пчеле, второе – к слону. Класс реализует следующие методы: – fly() – может летать – возвращает True,
 если часть пчелы не меньше части слона, иначе False; – trumpet() – трубить – если часть слона не меньше части пчелы,
 возвращает строку:
 “tu-tu-doo-doo!”, иначе “wzzzzz”. – eat(meal, value) – есть – может есть только нектар (nectar) или траву (grass).
  Если съедает нектар,то из части слона вычитается количество съеденного, пчеле добавляется, иначе наоборот:
  у пчелы вычитается, а слону добавляется.Не может увеличиться выше 100 и уменьшиться меньше 0;
   – get_parts() – возвращает список из значений: [часть пчелы, часть слона]."""

class BeeElephant:
    def __init__(self,bee,elephant,nectar, grass):
        self.bee = bee
        self.elephant = elephant
        self.nectar = nectar
        self.grass = grass
    def fly(self):
        if self.bee >= self.elephant:
            return True
        else:
            return False
    def trumplet(self):
        if self.elephant >= self.bee:
            print('tu-tu-doo-doo!')
        else:
            print('wzzzzz')
    def eat(self,meal,value):
        if meal == self.nectar:
            self.bee + self.nectar
            self.elephant - self.grass
        if meal == self.grass:
            self.bee - self.grass
            self.elephant +self.grass
    def get_parts(self):
        print(['часть пчелы:',self.bee,'часть слона:',self.elephant])








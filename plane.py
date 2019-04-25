from aircraft import Aircraft
class Plane(Aircraft):
    def __init__(self, plane_id, owner):
        super().__init__()
        self.plane_id = plane_id
        self.owner = owner

Boeing_747_8 = Plane('BA74794', 'British Airways')
Boeing_747_400 = Plane('BA74734', 'British Airways')
Boeing_747_400ER = Plane('BA73721', 'Ryan Air')
Boeing_777_300 = Plane('BA77743', 'Air Lingus')
Boeing_777_300ER = Plane('BA77742', 'Easy Jet')

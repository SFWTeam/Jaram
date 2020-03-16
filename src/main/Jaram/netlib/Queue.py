# Jaram
# A MC:BE Software
# https://github.com/SFWTeam/Jaram
# By SFW-Team
# And GianC-Dev
# -------------------------------

class Queue:
    objects = []

    def get(self, index):
        return self.objects[index]

    def append(self, obj):
        self.objects.append(obj)

    def shift(self):
        try:
            return self.objects.pop(0)
        except IndexError:
            return None

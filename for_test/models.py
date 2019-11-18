from django.db import models

# Create your models here.
class test_db(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    latitude = models.CharField(max_length=15)
    longitude = models.CharField(max_length=15)
    equip_id = models.IntegerField()
    serial = models.FloatField()
    v1 = models.FloatField()
    v2 = models.FloatField()
    v3 = models.FloatField()
    v4 = models.FloatField()
    v5 = models.FloatField()
    v6 = models.FloatField()
    v7 = models.FloatField()
    v8 = models.FloatField()
    v9 = models.FloatField()
    v10 = models.FloatField()
    v11 = models.FloatField()
    v12 = models.FloatField()
    v13 = models.FloatField()
    v14 = models.FloatField()
    v15 = models.FloatField()
    v16 = models.FloatField()
    v17 = models.FloatField()
    v18 = models.FloatField()
    v19 = models.FloatField()
    v20 = models.FloatField()

    def __str__(self):
        return 'ID:{0} TIME:{1} GPS_lat:{2} GPS_long:{3} equipment_id:{4} Serial:{5} VALUES:({6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}, {21}, {22}, {23}, {24), {25})'.format(
                self.id, self.date, self.latitude, self.longitude, self.equip_id, self.Serial, 
                self.v1, self.v2, self.v3, self.v4, self.v5, 
                self.v6, self.v7, self.v8, self.v9, self.v10, 
                self.v11, self.v12, self.v13, self.v14, self.v15, 
                self.v16, self.v17, self.v18, self.v19, self.v20)



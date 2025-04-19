from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Goods(db.Model):
   __tablename__ = 'goods'
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(200)) # 
   description = db.Column(db.Text) # 
   price = db.Column(db.Integer) # 
   img = db.Column(db.String(200)) # 
   size = db.Column(db.Text) # 
   category = db.Column(db.String(200)) # 

   
   @property
   def serialize(self):
      """Возвращайте данные объекта в легко сериализуемом формате"""
      return {
            'id':self.id,
            'title':self.title,
            'description':self.description,
            'price':self.price,
            'img':self.img,
            'size':self.size,
            'category':self.category,
      }
      
   def __repr__(self):
       return {'id':self.id,'title':self.title,'description':self.description,'price':self.price,'img':self.img,'size':self.size,'category':self.category}
   




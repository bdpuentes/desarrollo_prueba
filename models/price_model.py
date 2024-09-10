from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Price(Base):
    __tablename__ = 'PRICES'

    brand_id = Column(Integer, primary_key=True)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    price_list = Column(Integer, nullable=False)
    product_id = Column(Integer, nullable=False)
    priority = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    curr = Column(String, nullable=False)

    def to_dict(self):
        return {
            'brand_id': self.brand_id,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'price_list': self.price_list,
            'product_id': self.product_id,
            'priority': self.priority,
            'price': self.price,
            'curr': self.curr
        }
from sqlalchemy import Column, Integer, String

from models.db.database import Database


class TrackerModel(Database.base):
    __tablename__ = 'trackers'

    id = Column(Integer, primary_key = True, autoincrement=True)
    tracker_id = Column(Integer, nullable=False)
    course = Column(String, nullable=False)
    assignment_name = Column(String, nullable=False)
    due_date = Column(String, nullable=False)
    due_time = Column(String, nullable=False)

    @classmethod
    def insert(self, tracker_id, course, assignment_name,
                    due_date, due_time, session):
        tracker_info = self(tracker_id=tracker_id, course=course,
                            assignment_name = assignment_name, due_date=due_date, 
                            due_time = due_time)
        
        session.add(tracker_info)
        session.commit()

        return tracker_info
    
    @classmethod
    def remove(cls, tracker_id, session):
        tracker_info = session.query(cls).filter_by(tracker_id=tracker_id).first()
        
        if tracker_info:
            session.delete(tracker_info)
            session.commit()
            return True
        else:
            return False
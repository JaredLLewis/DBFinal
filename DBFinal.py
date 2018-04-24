from flask import Flask, g, render_template, url_for, request
import pymysql
import datetime
from datetime import datetime
cursor = None
conn = None
if cursor and conn:
    cursor.close()
    conn.close()
conn = pymysql.connect(host="us-cdbr-iron-east-05.cleardb.net", user="bacde7f8db1310", password="ffe159d1",
                        database="heroku_29c05403ae453df")



app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')



@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/diagram')
def diagram():
    return render_template('diagram.html')
@app.route('/logicaldiagram')
def logicaldiagram():
    return render_template('logicaldiagram.html')

@app.route('/queries')
def queries():
    return render_template('queries.html')
@app.route('/query_post', methods=['GET', 'POST'])
def query_post():
    querynum = request.form.get('querycontroller')
    print(querynum)
    object = None
#
    if querynum == "1":
        while True:
            try:
                sql = 'SELECT ResidenceHallName, ResidenceHallManager, ResidenceHallPhone FROM residencehall'
                cursor = conn.cursor()
                cursor.execute(sql)
                cursor.close()
                object = [dict(ResidenceHallName=row[0], ResidenceHallManager=row[1], ResidenceHallPhone=row[2])
                        for row in cursor.fetchall()]
                break
            except:
                conn.ping(True)


    if querynum == "2":
        sql = 'SELECT student.StudentMUNumber, student.StudentFirstname, student.StudentLastName, lease.LeaseDuration, lease.DateEntered, lease.DateLeave, lease.Semester FROM Student INNER JOIN lease ON student.StudentMUNumber=lease.StudentMUNumber  ;'
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        object = [dict(StudentMUNumber=row[0], StudentFirstName=row[1], StudentLastName=row[2], LeaseDuration=row[3].strftime("%B %d, %Y"), LeaseDateEntered=row[4].strftime("%B %d, %Y"), LeaseDateLeave=row[5], Semester=row[6])
                  for row in cursor.fetchall()]
    if querynum == "3":
        sql = 'SELECT * FROM Lease WHERE Semester = "Summer";'
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        object = [dict(LeaseNumber=row[0], StudentMUNumber=row[1], PlaceNumber=row[2], LeaseDuration=row[3].strftime("%B %d, %Y"),
                       LeaseDateEntered=row[4].strftime("%B %d, %Y"), LeaseDateLeave=row[5], Semester=row[6])
                  for row in cursor.fetchall()]


    if querynum == "4":
        sql = 'SELECT SUM(InvoiceAmount), lease.LeaseNumber, lease.StudentMUNumber FROM invoice INNER JOIN lease ON invoice.LeaseNumber=lease.LeaseNumber WHERE lease.StudentMUNumber = "1"'

        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        object = [dict(SUM=row[0], LeaseNumber=row[1], StudentMUNumber = row[2])
                  for row in cursor.fetchall()]
    if querynum == "5":

        sql = 'SELECT student.StudentFirstName, student.StudentLastName, invoice.InvoicePaid, invoice.InvoicePaymentDue FROM student INNER JOIN lease on student.StudentMUNumber=lease.studentMUNumber INNER JOIN invoice ON invoice.LeaseNumber=lease.LeaseNumber WHERE invoice.InvoicePaid = "0" AND invoice.InvoicePaymentDue <= "2019-04-22 21:40:18.351" '
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        object = [dict(StudentFirstName=row[0], StudentLastName=row[1], InvoicePaid=row[2], InvoicePaymentDue=row[3])
                  for row in cursor.fetchall()]
    if querynum == "6":
        sql = 'SELECT InspectionNumber, ApartmentNumber, StaffNumber, InspectionInspectionGood, InspectionDate, InspectionComments FROM studentapartmentinspections WHERE InspectionInspectioNGood ="0"'

        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        object = [dict(InspectionNumber=row[0], ApartmentNumber=row[1], StaffNumber=row[2], InspectionInspectionGood=row[3], InspectionDate=row[4], InspectionComments=row[5])
                  for row in cursor.fetchall()]
    if querynum == "7":

        sql = 'SELECT student.StudentMUNumber, student.StudentFirstName, student.StudentLastName, room.PlaceNumber, room.RoomNumber FROM student INNER JOIN lease on student.StudentMUNumber=lease.studentMUNumber INNER JOIN room ON lease.PlaceNumber=room.PlaceNumber WHERE room.ResidenceHallNumber = "1" '
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        object = [dict(StudentMUNumber=row[0], StudentFirstName=row[1], StudentLastName=row[2], PlaceNumber=row[3], RoomNumber=row[4])
                  for row in cursor.fetchall()]
    if querynum == "8":
        sql = 'SELECT StudentMUNumber, StudentFirstName, StudentLastName, StudentEmail, StudentCategory FROM student WHERE StudentStatus = "0"'

        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        object = [dict(StudentMUNumber=row[0], StudentFirstName=row[1], StudentLastName=row[2], StudentEmail=row[3],
                       StudentCategory=row[4])
                  for row in cursor.fetchall()]
    if querynum == "9":
        sql = 'SELECT StudentCategory, COUNT(*) AS TotalStudents FROM Student GROUP BY StudentCategory'

        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        object = [dict(StudentCategory=row[0], count=row[1])
                  for row in cursor.fetchall()]
    if querynum == "10":
        sql = 'SELECT student.StudentMUNumber, student.StudentFirstName, student.StudentLastName FROM student WHERE student.StudentMUNumber NOT IN (SELECT student.StudentMUNumber FROM student INNER JOIN nextofkin on student.StudentMUNumber=nextofkin.StudentMUNumber)'
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        object = [dict(StudentMUNumber=row[0], StudentFirstName=row[1], StudentLastName=row[2])
                  for row in cursor.fetchall()]
    if querynum == "11":
        sql = 'SELECT advisor.AdvisorFirstName, advisor.AdvisorLastName,advisor.AdvisorPhoneNumber, student.StudentMUNumber FROM advisor INNER JOIN student on advisor.StaffNumber=student.StaffNumber WHERE student.StudentMUNumber = "1"'

        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        object = [dict(AdvisorFirstName=row[0], AdvisorLastName=row[1], AdvisorPhoneNumber=row[2], StudentMUNumber=row[3])
                  for row in cursor.fetchall()]
    if querynum == "12":
        sql = 'SELECT MAX(MonthlyRentRate), MIN(MonthlyRentRate), ROUND(AVG(MonthlyRentRate), 2) AS AveragePrice FROM room WHERE room.ApartmentNumber="0"'

        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        object = [
            dict(MAX=row[0], MIN=row[1], AVG=row[2])
            for row in cursor.fetchall()]
    if querynum == "13":
        sql = 'SELECT COUNT(*) AS TotalRooms, residencehall.ResidenceHallName FROM room INNER JOIN residencehall on room.ResidenceHallNumber=residencehall.ResidenceHallNumber WHERE room.ResidenceHallNumber <> "0" GROUP BY room.ResidenceHallNumber '

        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        object = [
            dict(count=row[0], residenceHallName=row[1])
            for row in cursor.fetchall()]

    if querynum == "14":
        sql = 'SELECT StaffNumber, StaffFirstName,StaffLastName,StaffLocation, YEAR(CURRENT_TIMESTAMP) - YEAR(StaffDateOfBirth) - (RIGHT(CURRENT_TIMESTAMP, 5) < RIGHT(StaffDateOfBirth, 5)) as age  FROM residenceStaff WHERE YEAR(CURRENT_TIMESTAMP) - YEAR(StaffDateOfBirth) - (RIGHT(CURRENT_TIMESTAMP, 5) < RIGHT(StaffDateOfBirth, 5)) > "60"'

        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        object = [
            dict(StaffNumber=row[0], StaffFirstName=row[1], StaffLastName=row[2], StaffLocation=row[3], StaffAge=row[4])
            for row in cursor.fetchall()]
    if querynum == "15":
        sql = 'SELECT COUNT(VehicleNumber) as TotalRegistered, ParkingLotNumber FROM Vehicle WHERE ParkingLotNumber= "1";'

        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        object = [
            dict(count=row[0], ParkingLotNumber=row[1])
            for row in cursor.fetchall()]

    return render_template('query_post.html', object=object, querynum=querynum)


if __name__ == '__main__':
    app.debug = True
    app.run()




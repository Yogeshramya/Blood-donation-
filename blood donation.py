CREATE DATABASE BloodDonateDB;
USE BloodDonateDB;
CREATE TABLE Donors (
    DonorID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Age INT,
    BloodGroup VARCHAR(5),
    Contact VARCHAR(15),
    LastDonationDate DATE
);
CREATE TABLE Recipients (
    RecipientID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Age INT,
    BloodGroup VARCHAR(5),
    Contact VARCHAR(15),
    BloodRequired INT
);
CREATE TABLE Donations (
    DonationID INT AUTO_INCREMENT PRIMARY KEY,
    DonorID INT,
    BloodGroup VARCHAR(5),
    DonationDate DATE,
    FOREIGN KEY (DonorID) REFERENCES Donors(DonorID)
);

CREATE TABLE BloodInventory (
    BloodGroup VARCHAR(5) PRIMARY KEY,
    UnitsAvailable INT DEFAULT 0
);
CREATE TABLE Requests (
    RequestID INT AUTO_INCREMENT PRIMARY KEY,
    RecipientID INT,
    BloodGroup VARCHAR(5),
    UnitsRequested INT,
    RequestDate DATE,
    Status ENUM('Approved', 'Rejected', 'Pending'),
    FOREIGN KEY (RecipientID) REFERENCES Recipients(RecipientID)
);
DELIMITER //
CREATE TRIGGER AfterDonation
AFTER INSERT ON Donations
FOR EACH ROW
BEGIN
    UPDATE BloodInventory
    SET UnitsAvailable = UnitsAvailable + 1
    WHERE BloodGroup = NEW.BloodGroup;
END;
//
DELIMITER ;
INSERT INTO Donors (Name, Age, BloodGroup, Contact, LastDonationDate)
VALUES ('Abishek', 28, 'O+', '9876543210', '2025-03-01');
INSERT INTO Recipients (Name, Age, BloodGroup, Contact, BloodRequired)
VALUES ('Madhan', 35, 'O+', '9898989898', 2);
INSERT INTO Donations (DonorID, BloodGroup, DonationDate)
VALUES (1, 'O+', '2025-03-20');
SELECT UnitsAvailable FROM BloodInventory WHERE BloodGroup = 'O+';
INSERT INTO BloodInventory (BloodGroup, UnitsAvailable)
VALUES 
('O+', 5), ('A+', 5), ('B+', 3), ('AB+', 6),
('O-', 2), ('A-', 1), ('B-', 0), ('AB-', 0);
SELECT * FROM BloodInventory;
SELECT Donors.Name, Donations.BloodGroup, Donations.DonationDate
FROM Donations
JOIN Donors ON Donations.DonorID = Donors.DonorID;

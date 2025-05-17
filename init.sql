CREATE DATABASE IF NOT EXISTS sqli_lab;
USE sqli_lab;

CREATE TABLE users (
  idx INT AUTO_INCREMENT PRIMARY KEY,
  userid VARCHAR(100) NOT NULL,
  userpw VARCHAR(100) NOT NULL
);

INSERT INTO users (userid, userpw) VALUES ('admin', 'hello'), ('guest', 'world'), ('daniel', 'lion');

CREATE TABLE posts (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255),
  content TEXT,
  author VARCHAR(255)
);

INSERT INTO posts (title, content, author) VALUES
('환영합니다', '이 게시판은 테스트용입니다', 'admin'),
('관리자 공지', '비밀 내용 없음', 'admin'),
('SQL Injection?', '해볼 수 있을까요?', 'guest');

CREATE TABLE svalue (
  idx INT AUTO_INCREMENT PRIMARY KEY,
  sflag VARCHAR(255)
);

INSERT INTO svalue (sflag) VALUES ('FLAG{YouAreGood}');

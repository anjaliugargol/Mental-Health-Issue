-- =====================================================
-- 🧠 Mental Health Database Schema
-- =====================================================

-- Create Database
CREATE DATABASE IF NOT EXISTS mental_health;

-- Use Database
USE mental_health;

-- Create Table
CREATE TABLE IF NOT EXISTS mental_h (
    id INT AUTO_INCREMENT PRIMARY KEY,
    statement TEXT NOT NULL,
    status VARCHAR(50) NOT NULL,
    text_length INT,
    word_count INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

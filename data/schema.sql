-- NeoNeX MindX Central Database Schema
-- Target: PostgreSQL 14+ / Supabase / AWS RDS

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 1. USERS & ROLES (Admin CMS, Counselor CRM, Tutors)
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(150) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(50) DEFAULT 'counselor', -- 'superadmin', 'cms_editor', 'counselor', 'tutor'
    phone VARCHAR(30),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2. LEADS & INQUIRIES (Incoming from Website & Modal Popup)
CREATE TABLE IF NOT EXISTS leads (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    candidate_name VARCHAR(150) NOT NULL,
    phone VARCHAR(30) NOT NULL,
    email VARCHAR(255),
    program VARCHAR(150) NOT NULL,
    current_role VARCHAR(150),
    skill_level VARCHAR(50),
    preferred_batch VARCHAR(100),
    learning_goal TEXT,
    source_page VARCHAR(255),
    status VARCHAR(50) DEFAULT 'New', -- 'New', 'Contacted', 'Counselled', 'Demo Booked', 'Enrolled', 'Lost'
    assigned_to UUID REFERENCES users(id) ON DELETE SET NULL,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 3. COURSES (Synced with Website & CMS)
CREATE TABLE IF NOT EXISTS courses (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    slug VARCHAR(150) UNIQUE NOT NULL,
    title VARCHAR(200) NOT NULL,
    category VARCHAR(100),
    duration VARCHAR(50),
    fee NUMERIC(10, 2),
    syllabus_url TEXT,
    is_published BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 4. BATCHES (Scheduled by Admin / CRM)
CREATE TABLE IF NOT EXISTS batches (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    course_id UUID REFERENCES courses(id) ON DELETE CASCADE,
    batch_name VARCHAR(150) NOT NULL,
    start_date DATE NOT NULL,
    timings VARCHAR(100) NOT NULL,
    mode VARCHAR(50) DEFAULT 'Live Online', -- 'Live Online', 'Classroom'
    capacity INT DEFAULT 30,
    enrolled_count INT DEFAULT 0,
    status VARCHAR(50) DEFAULT 'Upcoming', -- 'Upcoming', 'Ongoing', 'Completed'
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 5. STUDENTS & ENROLLMENTS (Conversions from Leads)
CREATE TABLE IF NOT EXISTS students (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    lead_id UUID REFERENCES leads(id) ON DELETE SET NULL,
    full_name VARCHAR(150) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(30) NOT NULL,
    enrolled_course_id UUID REFERENCES courses(id) ON DELETE RESTRICT,
    batch_id UUID REFERENCES batches(id) ON DELETE SET NULL,
    total_fee NUMERIC(10, 2),
    paid_fee NUMERIC(10, 2) DEFAULT 0.00,
    enrollment_status VARCHAR(50) DEFAULT 'Active', -- 'Active', 'Completed', 'Dropped'
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 6. PAYMENTS & TRANSACTIONS
CREATE TABLE IF NOT EXISTS payments (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    student_id UUID REFERENCES students(id) ON DELETE CASCADE,
    amount NUMERIC(10, 2) NOT NULL,
    payment_mode VARCHAR(50), -- 'Razorpay', 'UPI', 'NetBanking', 'Card'
    transaction_id VARCHAR(120),
    status VARCHAR(50) DEFAULT 'Successful',
    receipt_url TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance
CREATE INDEX IF NOT EXISTS idx_leads_created ON leads(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_leads_status ON leads(status);
CREATE INDEX IF NOT EXISTS idx_courses_slug ON courses(slug);

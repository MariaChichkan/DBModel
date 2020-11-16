from sqlalchemy import Column, String, Integer, BOOLEAN, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class LogTable(Base):
    __tablename__ = 'all_json'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    one_string = Column('feature_id', String(1000))

    def __init__(self, one_string):
        self.one_string = one_string


class FeatureDescriptionRow(Base):
    __tablename__ = 'mega_features_description'
    feature_id = Column('feature_id', String(50), primary_key=True)
    name = Column('name', String(1000))
    user = Column('user', String(50))
    created = Column('created', String(50))
    updated = Column('updated', String(50))

    def __init__(self, feature_id, name, user, created, updated):
        self.feature_id = feature_id
        self.name = name
        self.user = user
        self.created = created
        self.updated = updated


class RequestRelease(Base):
    __tablename__ = 'requests_to_release'
    application_id = Column('application_id', String(50), primary_key=True)
    application_key = Column('application_key', String(50))
    feature_id = Column('feature_id', String(50))
    platform = Column('platform', String(50))
    release_id = Column('release_id', String(50))
    release_key = Column('release_key', String(50))
    segment = Column('segment', String(50))
    request_type = Column('request_type', String(50))
    status = Column('status', String(50))

    def __init__(self,application_id, application_key, feature_id, platform, release_id, release_key, segment,
                 request_type, status):
        self.application_id = application_id
        self.application_key = application_key #new
        self.feature_id = feature_id
        self.platform = platform
        self.release_id = release_id
        self.release_key = release_key
        self.segment = segment
        self.request_type = request_type
        self.status = status


class RelationRelFeature(Base):
    __tablename__ = 'relation_release_feature'
    application_id = Column('application_id', String(50), primary_key=True)
    platform = Column('platform', String(50))
    feature_name = Column('feature_name', String(50))
    story_key = Column('story_key', String(50))
    release_key = Column('release_key', String(50))
    type = Column('type', String(50))
    result = Column('result', String(50))
    error_code = Column('error_code', String(50))
    last_update = Column('last_update', String(50))

    def __init__(self, application_id, platform, feature_name, release_key, story_key, type, result, error_code,
                 last_update):
        self.application_id = application_id
        self.platform = platform
        self.feature_name = feature_name
        self.release_key = release_key
        self.story_key = story_key
        self.type = type
        self.result = result
        self.error_code = error_code
        self.last_update = last_update


class RelationSwellFeature(Base):
    __tablename__ = 'relation_swell_feature'
    application_id = Column('application_id', String(50), primary_key=True)
    platform = Column('platform', String(50))
    feature_name = Column('feature_name', String(50))
    swell_key = Column('swell_key', String(50))
    release_key = Column('release_key', String(50))
    request_type = Column('request_type', String(50))
    result = Column('result', String(50))
    error_code = Column('error_code', String(50))
    last_update = Column('last_update', String(50))
    channel = Column('channel', String(50))

    def __init__(self, application_id, platform,  feature_name, swell_key, release_key, request_type, result, error_code,
                 last_update, channel):
        self.application_id = application_id
        self.platform = platform
        self.feature_name = feature_name
        self.swell_key = swell_key
        self.release_key = release_key
        self.request_type = request_type
        self.result = result
        self.error_code = error_code
        self.last_update = last_update
        self.channel = channel



class ReleaseRow(Base):
    __tablename__ = 'release'
    release_id = Column('release_id', String(50), primary_key=True)  # Уникальный идентификатор релиза
    name = Column('name', String(50))  # Наименование релиза
    platform = Column('platform', String(50))  # Платформа
    jira_key = Column('jira_key', String(50))  # Ключ релиза в jira
    status = Column('status', String(50))

    def __init__(self, release_id, name, platform, jira_key, status ):
        self.release_id = release_id
        self.name = name
        self.platform = platform
        self.jira_key = jira_key
        self.status = status

class ReleaseDates(Base):  # Даты релизов
    __tablename__ = 'releasedates'
    release_id = Column('release_id', String(50), primary_key=True)
    date_type = Column('date_type', String(50), primary_key=True)
    platform = Column('platform', String(50))  # Платформа
    date = Column('date', String(50))

    def __init__(self, release_id, platform, date_type, date):
        self.release_id = release_id
        self.platform = platform
        self.date_type = date_type
        self.date = date



        
class EribRequest(Base):
    __tablename__ = 'erib_table'
    feature_id = Column('feature_id', String(50), primary_key=True)

    def __init__(self, feature_id):
        self.feature_id = feature_id
        
        

class DOR(Base):
    __tablename__ = 'dor'
    application_id = Column('application_id', String(50), primary_key=True)
    subtask_key = Column('subtask_key', String(50), primary_key=True)
    dor_type_id = Column('dor_type_id',  String(50))
    content = Column('content',  String(1000))
    status = Column('status', String(50))
    user = Column('user', String(50))
    assignee_key = Column('assignee_key', String(50))
    assignee_name = Column('assignee_name', String(50))
    assignee_email = Column('assignee_email', String(50)) 
    last_update = Column('last_update', String(50))

    def __init__(self, application_id, subtask_key, dor_type_id,  content, status,  user, assignee_key, assignee_name, assignee_email,  last_update):
        self.application_id = application_id
        self.subtask_key = subtask_key
        self.dor_type_id = dor_type_id
        self.content = content
        self.status = status
        self.user = user
        self.assignee_key = assignee_key
        self.assignee_name = assignee_name
        self.assignee_email = assignee_email
        self.last_update = last_update
        
           
        
class DORInformation(Base):
    __tablename__ = 'dor_info' 
    dor_type_id = Column('dor_type_id', String(50), primary_key=True)
    category =  Column('category', String(500))
    dor_name = Column('dor_name', String(1000))
    short_name = Column('short_name', String(100))
    short_description = Column('short_description', String(1000))
    upper_text = Column('upper_text', String(1000))
    description = Column('description', String(1000))
    placeholder = Column('placeholder', String(1000))
    label = Column('label', String(50))
    dor_type = Column('dor_type', String(50))
    close_date = Column('close_date', String(50))
    close_text = Column('close_text', String(1000))
    show_in_details = Column("show_in_details" , String(50))
    active = Column("active", String(50))

    def __init__(self, dor_type_id, category,  dor_name, short_name, short_description, upper_text, description, placeholder, label,  dor_type, close_date, close_text,  show_in_details, active):
        self.dor_type_id = dor_type_id
        self.category = category
        self.dor_name = dor_name
        self.short_name = short_name
        self.short_description = short_description
        self.upper_text = upper_text
        self.description = description
        self.placeholder = placeholder
        self.label = label
        self.dor_type =  dor_type
        self.close_date = close_date
        self.close_text = close_text
        self.show_in_details = show_in_details
        self.active = active
          
class Bugs(Base):
    __tablename__ = 'bugs' 
    key = Column('key', String(50), primary_key=True)
    platform = Column('platform', String(50), primary_key=True)
    project = Column('project', String(50))
    status =  Column('status', String(50))
    name = Column('name', String(500))
    priority = Column('priority', String(50))
    def __init__(self, key, platform, project, status, name,  priority):
        self.key = key
        self.platform = platform
        self.project = project
        self.status = status
        self.name = name
        self.priority = priority
        
class TeamBugs(Base):
    __tablename__ = 'team_bugs' 
    project = Column('project', String(50), primary_key=True)
    platform = Column('platform', String(50), primary_key=True)
    priority = Column('priority', String(50), primary_key=True)
    number_of_bugs = Column('number_of_bugs', String(50))
    def __init__(self, project, platform, priority, number_of_bugs):
        self.project = project
        self.platform = platform
        self.priority = priority
        self.number_of_bugs = number_of_bugs


class ProjectDescription(Base):
    __tablename__ = 'project_description'
    key = Column('key', String(50), primary_key=True)
    name = Column('name', String(500))
    category = Column('category', String(50))
    description = Column('description', String(1000))

    def __init__(self, key, name, category, description):
        self.key = key
        self.name = name
        self.category = category
        self.description = description

class MassFeature(Base):
    __tablename__ = 'mass_feature'
    id = Column('id', String(50), primary_key=True)
    key = Column('key', String(50))
    name = Column('name', String(500))
    type = Column('type', String(50))
    content = Column('content', String(1000))

    def __init__(self, id, key, name, type, content):
        self.id = id
        self.key = key
        self.name = name
        self.type = type
        self.content = content

class MassFeatureLink(Base):
    __tablename__ = 'mass_features_link'
    mass_id = Column('mass_id', String(50), primary_key=True)
    mass_key = Column('mass_key', String(50))
    release_key = Column('release_key', String(50))

    def __init__(self, mass_id, mass_key, release_key):
        self.mass_id = mass_id
        self.mass_key = mass_key
        self.release_key = release_key


class ReleasePages(Base):
    __tablename__ = 'release_pages'
    release_id = Column('release_id', String(50), primary_key=True)
    page = Column('page', String(50))

    def __init__(self, release_id, page):
        self.release_id = release_id
        self.page = page


class ApplicationQuantity(Base):
    __tablename__ = 'application_quantity'
    release_id = Column('release_id', String(50), primary_key=True)
    teams = Column('teams', String(50))
    applications = Column('applications', String(50))
    applications_psi_ready =  Column('applications_psi_ready', String(50))
    applications_psi_not_ready = Column('applications_psi_not_ready', String(50))
    applications_psi_passed = Column('applications_psi_passed', String(50))
    applications_canceled = Column('applications_canceled', String(50))
    updated = Column('updated', String(50))

    def __init__(self, release_id, teams, applications, applications_psi_ready, applications_psi_not_ready,
                 applications_psi_passed, applications_canceled, updated):
        self.release_id = release_id
        self.teams = teams
        self.applications = applications
        self.applications_psi_ready = applications_psi_ready
        self.applications_psi_not_ready = applications_psi_not_ready
        self.applications_psi_passed = applications_psi_passed
        self.applications_canceled = applications_canceled
        self.updated = updated


class ApplicationStatus(Base):
    __tablename__ = 'application_status'
    status = Column('status', String(50), primary_key=True)
    platform = Column('platform', String(50), primary_key=True)
    jira_status = Column('jira_status', String(50))
    name = Column('name', String(500))

    def __init__(self, status, platform, jira_status, name):
        self.status = status
        self.platform = platform
        self.jira_status = jira_status
        self.name = name


class AndroidExtraInfo(Base):
    __tablename__ = 'android_extra_info'
    release_id = Column('release_id', String(50), primary_key=True)
    implement = Column('implement', String(50))
    failures = Column('failures', String(50))
    crashes_devices_coeffi = Column('crashes_devices_coeffi', String(50))
    installations = Column('installations', String(50))
    number_ratings = Column('number_ratings', String(50))
    ratings = Column('ratings', String(50))
    crash_free_users_text = Column('crash_free_users_text', String(50))
    crash_free_sessions_text = Column('crash_free_sessions_text', String(50))
    active_users_percentage = Column('active_users_percentage', String(50))
    crashes_per_ten_thousand_users = Column('crashes_per_ten_thousand_users', String(50))
    users_app_metrica = Column('users_app_metrica', String(50))
    sessions_app_metrica = Column('sessions_app_metrica', String(50))

    def __init__(self, release_id, implement, failures, crashes_devices_coeffi, installations, number_ratings, ratings, crash_free_users_text,
                 crash_free_sessions_text, active_users_percentage, crashes_per_ten_thousand_users, users_app_metrica,sessions_app_metrica ):
        self.release_id = release_id
        self.implement = implement
        self.failures = failures
        self.crashes_devices_coeffi = crashes_devices_coeffi
        self.installations = installations
        self.number_ratings = number_ratings
        self.ratings = ratings
        self.crash_free_users_text = crash_free_users_text
        self.crash_free_sessions_text = crash_free_sessions_text
        self.active_users_percentage = active_users_percentage
        self.crashes_per_ten_thousand_users = crashes_per_ten_thousand_users
        self.users_app_metrica = users_app_metrica
        self.sessions_app_metrica = sessions_app_metrica


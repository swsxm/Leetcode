SELECT DISTINCT viewer_id as id FROM Views
where viewer_id = author_id
ORDER by id ASC;

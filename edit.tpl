<!DOCTYPE html>
<html>
<head>
    <title>Edit Vehicle</title>
</head>
<body>
    <h1>Edit Vehicle</h1>
    <form action="/edit/{{ vehicle[0] }}" method="post">
        <label>Title:</label>
        <input type="text" name="title" value="{{ vehicle[1] }}" required><br>
        <label>Release Year:</label>
        <input type="number" name="release_year" value="{{ vehicle[2] }}" required><br>
        <label>Companion:</label>
        <select name="companion_id">
            % for companion in companions:
            % if companion[0] == vehicle[3]:
            <option value="{{ companion[0] }}" selected>{{ companion[1] }}</option>
            % else:
            <option value="{{ companion[0] }}">{{ companion[1] }}</option>
            % end
            % end
        </select><br>
        <input type="submit" value="Save">
    </form>
    <p><a href="/">Back to List</a></p>
</body>
</html>

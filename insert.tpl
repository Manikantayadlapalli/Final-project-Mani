<!DOCTYPE html>
<html>
<head>
    <title>Add Vehicle</title>
</head>
<body>
    <h1>Add Vehicle</h1>
    <form action="/add" method="post">
        <label>Title:</label>
        <input type="text" name="title" required><br>
        <label>Release Year:</label>
        <input type="number" name="release_year" required><br>
        <label>Companion:</label>
        <select name="companion_id">
            % for companion in companions:
            <option value="{{ companion[0] }}">{{ companion[1] }}</option>
            % end
        </select><br>
        <input type="submit" value="Add">
    </form>
    <p><a href="/">Back to List</a></p>
</body>
</html>

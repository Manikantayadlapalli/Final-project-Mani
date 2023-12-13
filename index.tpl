<!DOCTYPE html>
<html>
<head>
    <title>Vehicles and Companions</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }

        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }
    </style>
</head>
<body>
    <form action="/" method="get">
        <label>Search:</label>
        <input type="text" name="search" placeholder="Enter title or company">
        <input type="submit" value="Search">
    </form>

    <h1>Vehicles and Companions</h1>
    <table>
        <tr>
            <th>S.NO</th>
            <th>Model</th>
            <th>Release Year</th>
            <th>Company</th>
            <th>Edit</th>
            <th>Delete</th>
        </tr>
        % for vehicle in vehicles:
        <tr>
            <td>{{ vehicle[0] }}</td>
            <td>{{ vehicle[1] }}</td>
            <td>{{ vehicle[2] }}</td>
            <td>{{ vehicle[3] }}</td>
            <td><a href="/edit/{{ vehicle[0] }}">Edit</a></td>
            <td><a href="/delete/{{ vehicle[0] }}" onclick="return confirm('Are you sure you want to delete this item?');">Delete</a></td>
        </tr>
        % end
    </table>

    <p><a href="/add">Add Vehicle</a></p>
</body>
</html>

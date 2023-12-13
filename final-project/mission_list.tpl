<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mission List</title>
</head>
<body>
    <h1>Mission List</h1>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Destination</th>
            <th>Spacecraft ID</th>
            <th>Action</th>
        </tr>
        % for mission in mission_list:
        <tr>
            <td>{{ mission.id }}</td>
            <td>{{ mission.name }}</td>
            <td>{{ mission.destination }}</td>
            <td>{{ mission.spacecraft_id }}</td>
            <td>
                <a href="/mission/edit/{{ mission.id }}">Edit</a>
                <a href="/mission/delete/{{ mission.id }}" onclick="return confirm('Are you sure?')">Delete</a>
            </td>
        </tr>
        % end
    </table>
    <p><a href="/mission/add">Add New Mission</a></p>
</body>
</html>


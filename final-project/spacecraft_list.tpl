<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Spacecraft List</title>
</head>
<body>
    <h1>Spacecraft List</h1>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Manufacturer</th>
            <th>Action</th>
        </tr>
        % for spacecraft in spacecraft_list:
        <tr>
            <td>{{ spacecraft.id }}</td>
            <td>{{ spacecraft.name }}</td>
            <td>{{ spacecraft.manufacturer }}</td>
            <td>
                <a href="/spacecraft/edit/{{ spacecraft.id }}">Edit</a>
                <a href="/spacecraft/delete/{{ spacecraft.id }}" onclick="return confirm('Are you sure?')">Delete</a>
            </td>
        </tr>
        % end
    </table>
    <p><a href="/spacecraft/add">Add New Spacecraft</a></p>
</body>
</html>



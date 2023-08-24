select x, y, z, (
    case
        when (
            x < y + z and
            y < x + z and
            z < x + y and
            x > 0 and y > 0 and z > 0
        ) then "Yes"
        else "No"
    end
) as triangle
from Triangle;
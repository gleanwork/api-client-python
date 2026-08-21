# CalendarRoomBookingStatus

The current booking status of the room resource associated with an event.

## Example Usage

```python
from glean.api_client.models import CalendarRoomBookingStatus

value = CalendarRoomBookingStatus.NONE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `NONE`     | NONE       |
| `ACCEPTED` | ACCEPTED   |
| `DECLINED` | DECLINED   |
| `PENDING`  | PENDING    |
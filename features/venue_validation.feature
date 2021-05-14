Feature: Venue Boundaries

Scenario Outline: Exceeding Venue Boundaries
    Given the venue <Venue>
    And an booking size of <Amount of Peeps>
    Then venue_capacity_valition should return <Expected Outcome>

Examples: Breached Capacity
|Venue       | Amount of Peeps | Expected Outcome |
|Music Room  |       45        |       Pass       |
|Music Room  |       50        |       Pass       |
|Music Room  |       51        |       Fail       |
|Music Room  |       51        |       Fail       |
|Coastlands Theatre | 331 | Pass |
|Coastlands Theatre | 330 | Pass |
|Coastlands Theatre | 336 | Fail |
|Coastlands Theatre | 332 | Fail |
|Blackbox Theatre | 200 | Pass |
|Blackbox Theatre | 199 | Pass |
|Blackbox Theatre | 201 | Fail |
|Blackbox Theatre | 206 | Fail |


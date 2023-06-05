
result = {"pesho": 12, "ivan": 16, "gosho": 10}
members = list(sorted(result.items(), key=lambda x: (-x[1], x[0])))
#result.extend([f"Member: {x[0]} - {x[1]}-years old" for x in members])
for name, age in members:
    print(f"name {name} age{age}")

from unittest import TestCase, main
from team_unit_tests.project.team import Team


class Test(TestCase):
    def setUp(self) -> None:
        self.team = Team("Team")

    def test_team_init(self):
        team_name = "Team"
        team = Team(team_name)

        self.assertEqual(team_name, team.name)
        self.assertEqual({}, team.members)

    def test_name_setter_raises_when_name_contains_non_alpha_letters(self):
        with self.assertRaises(ValueError) as context:
            team = Team("123asdASD.,$@!$%?!")
        self.assertEqual("Team Name can contain only letters!", str(context.exception))

    def test_add_member_adds_only_new_players_to_the_team(self):
        self.team.members["ivan"] = 18
        result = self.team.add_member(ivan=18, pesho=21, gosho=19, josh=16)
        self.assertEqual("Successfully added: pesho, gosho, josh", result)
        self.assertEqual(21, self.team.members["pesho"])
        self.assertEqual(19, self.team.members["gosho"])
        self.assertEqual(16, self.team.members["josh"])

    def test_remove_member_returns_error_message_when_player_does_not_exist(self):
        member_name = "Gosho"
        result = self.team.remove_member(member_name)
        self.assertEqual(f"Member with name {member_name} does not exist", result)

    def test_remove_member_removes_member_from_the_team(self):
        member_to_remove = "gosho"
        self.team.members["pesho"] = 21
        self.team.members[member_to_remove] = 19

        result = self.team.remove_member(member_to_remove)
        self.assertEqual(f"Member {member_to_remove} removed", result)
        self.assertEqual(21, self.team.members["pesho"])
        self.assertTrue(member_to_remove not in self.team.members)

    def test_gt_compares_team_by_members_count(self):
        self.team.members["member1"] = 18
        self.team.members["member2"] = 19

        another_team = Team("Another")
        another_team.members["member1"] = 21
        another_team.members["member2"] = 22
        another_team.members["member3"] = 23

        self.assertEqual(True, another_team > self.team)
        self.assertEqual(False, self.team > another_team)

    def test_len_returns_members_count(self):
        self.team.members["member1"] = 18
        self.team.members["member2"] = 19

        self.assertEqual(2, len(self.team))

    def test_add_returns_new_team_with_combined_members(self):
        self.team.members["member1"] = 18
        self.team.members["member2"] = 19

        another_team = Team("Another")
        another_team.members["member3"] = 21
        another_team.members["member4"] = 22
        another_team.members["member5"] = 23

        result = self.team + another_team
        expected_result_members = {
            "member1": 18,
            "member2": 19,
            "member3": 21,
            "member4": 22,
            "member5": 23,
        }
        self.assertEqual("TeamAnother", result.name)
        self.assertEqual(expected_result_members, result.members)

    def test_str_returns_members_sorted_in_descending_order_by_age_in_proper_string_format(self):
        self.team.members["member2"] = 19
        self.team.members["member1"] = 18
        self.team.members["member3"] = 20

        result = str(self.team)
        expected = f"Team name: Team\n" + \
               f"Member: member3 - 20-years old\n" + \
               f"Member: member2 - 19-years old\n" + \
               f"Member: member1 - 18-years old"

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()


import os, sys
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True
from template import *
__author__ = 'george'

N = Many()
E = Many()

n1 = N + HardGoal(
  "CS Be Not for Profit",
  "IT Department"
)

n2 = N + SoftGoal(
  "Properly and Suitably equipped in IT",
  "IT Department"
)

n3 = N + SoftGoal(
  "Increase IT Resources",
  "IT Department"
)

n4 = N + Resource(
  "IT Resources",
  "IT Department"
)

n5 = N + SoftGoal(
  "Web Services Self Serve",
  "CS Services"
)

n6 = N + SoftGoal(
  "Encourage Kids Using Web Services to Use Phone Services",
  "CS Services"
)

n7 = N + SoftGoal(
  "Maintain Services above Competition",
  "CS Services"
)

n8 = N + SoftGoal(
  "Empowering Kids to Help Themselves",
  "CS Services"
)

n9 = N + SoftGoal(
  "Increase Development of Public Education Program",
  "Public Education Program"
)

n10 = N + SoftGoal(
  "Measure Success of Services",
  "CS Services"
)

n11 = N + HardGoal(
  "Services Be Bilingual",
  "CS Services"
)

n12 = N + SoftGoal(
  "Reduce Contagion Effect [Of Harmful Actions]",
  "CS Services"
)

n13 = N + HardGoal(
  "Success Be Tracked in Community Resources",
  "Community Resource"
)

n14 = N + SoftGoal(
  "Avoid Presence of Pedofiles",
  "CS Services"
)

n15 = N + SoftGoal(
  "Increase Resources [Services]",
  "CS Services"
)

n16 = N + SoftGoal(
  "*High Quality Services",
  "CS Services"
)

n17 = N + SoftGoal(
  "Improve Image to Kids",
  "CS Services"
)

n18 = N + Task(
  "Maintain/Implement CS Services",
  "CS Services"
)

n19 = N + Task(
  "Maintain Web Services",
  "CS Services"
)

n20 = N + Task(
  "*Maintain Phone Services",
  "CS Services"
)

n21 = N + Task(
  "Maintain/ Implement PHL Services",
  "CS Services"
)

n22 = N + SoftGoal(
  "*Increase Number of Services",
  "CS Services"
)

n23 = N + SoftGoal(
  "Efficient Services",
  "CS Services"
)

n24 = N + SoftGoal(
  "Available [Services]",
  "CS Services"
)

n25 = N + Resource(
  "Service Resources",
  "CS Services"
)

n26 = N + Resource(
  "Regional Office Resources",
  "Regional Offices"
)

n27 = N + SoftGoal(
  "Improve Image to Kids",
  "SA Program"
)

n28 = N + SoftGoal(
  "Increased SA Resources",
  "SA Program"
)

n29 = N + SoftGoal(
  "Trust [of Kids]",
  "SA Program"
)

n30 = N + SoftGoal(
  "Quality SA Services",
  "SA Program"
)

n31 = N + SoftGoal(
  "Reduce Misconceptions",
  "SA Program"
)

n32 = N + SoftGoal(
  "Improve Image to Kids",
  "Marketing"
)

n33 = N + Resource(
  "Counselling Resources",
  "Counselling Management"
)

n34 = N + SoftGoal(
  "Positive Internal Opinion",
  "Counselling Management"
)

n35 = N + SoftGoal(
  "Increase Counselling Resource",
  "Counselling Management"
)

n36 = N + SoftGoal(
  "Increase Funding for Training",
  "Counselling Management"
)

n37 = N + SoftGoal(
  "Reduce Cost of Counselling HR",
  "Counselling Management"
)

n38 = N + SoftGoal(
  "Accountability of services",
  "Counselling Management"
)

n39 = N + SoftGoal(
  "*Help as many kids as possible",
  "Counselling Management"
)

n40 = N + HardGoal(
  "Research on kids be required",
  "Research Partners"
)

n41 = N + SoftGoal(
  "*High Quality Counselling",
  "Counselling"
)

n42 = N + SoftGoal(
  "Help Kids",
  "Counselling"
)

n43 = N + SoftGoal(
  "Avoid Liability Problems",
  "Counselling"
)

n44 = N + SoftGoal(
  "Reduce Contagion Effect [Of Harmful Actions]",
  "Counselling"
)

n45 = N + SoftGoal(
  "Responsible Usage [Sponsor Funds]",
  "Counselling"
)

n46 = N + Resource(
  "Funds",
  "Fund Development"
)

n47 = N + Resource(
  "Counsellor Experience",
  "Counselling"
)

n48 = N + Resource(
  "Caller Statistics",
  "Counselling"
)

n49 = N + SoftGoal(
  "Accountability of services",
  "Individual donor"
)

n50 = N + SoftGoal(
  "Demonstrable services",
  "Corporate Sponsors"
)

n51 = N + SoftGoal(
  "Increase Volunteers",
  "Fund Development"
)

n52 = N + SoftGoal(
  "Increase [Awareness]",
  "Marketing"
)

n53 = N + SoftGoal(
  "Avoid Over-Marketing Services",
  "Marketing"
)

n54 = N + SoftGoal(
  "Positive[Reputation of CS]",
  "Marketing"
)

n55 = N + SoftGoal(
  "Match Fundraising Targets",
  "Marketing"
)

n56 = N + SoftGoal(
  "Follow Highest Ethical Guidelines",
  "Corporate Sponsors"
)

n57 = N + SoftGoal(
  "Credibility [CS Brand]",
  "Corporate Sponsors"
)

n58 = N + SoftGoal(
  "Long Term Funding",
  "Fund Development"
)

n59 = N + Resource(
  "Information",
  "General Public"
)

n60 = N + HardGoal(
  "Services Be Free",
  "Parents, Kids & Youth"
)

n61 = N + HardGoal(
  "Collaborate with Not for Profit Partners on Services",
  "Not For Profit Partners"
)

n62 = N + HardGoal(
  "Involve CS in Events",
  "Not For Profit Partners"
)

#### INNERS
# TODO
n63 = N + HardGoal(
  "CS Be Not for Profit",
  "CS"
)

n64 = N + SoftGoal(
  "Properly and Suitably equipped in IT",
  "CS"
)

n65 = N + SoftGoal(
  "Increase IT Resources",
  "CS"
)

n66 = N + SoftGoal(
  "Web Services Self Serve",
  "CS"
)

n67 = N + SoftGoal(
  "Encourage Kids Using Web Services to Use Phone Services",
  "CS"
)

n68 = N + SoftGoal(
  "Maintain Services above Competition",
  "CS"
)

n69 = N + SoftGoal(
  "Empowering Kids to Help Themselves",
  "CS"
)

n70 = N + SoftGoal(
  "Increase Development of Public Education Program",
  "CS"
)

n71 = N + SoftGoal(
  "Measure Success of Services",
  "CS"
)

n72 = N + HardGoal(
  "Services Be Bilingual",
  "CS"
)

n73 = N + SoftGoal(
  "Reduce Contagion Effect [Of Harmful Actions]",
  "CS"
)

n74 = N + HardGoal(
  "Success Be Tracked in Community Resources",
  "CS"
)

n75 = N + SoftGoal(
  "Avoid Presence of Pedofiles",
  "CS"
)

n76 = N + SoftGoal(
  "Increase Resources [Services]",
  "CS"
)

n77 = N + SoftGoal(
  "*High Quality Services",
  "CS"
)

n78 = N + SoftGoal(
  "Improve Image to Kids",
  "CS"
)

n79 = N + Task(
  "Maintain/Implement CS Services",
  "CS"
)

n80 = N + Task(
  "Maintain Web Services",
  "CS"
)

n81 = N + Task(
  "*Maintain Phone Services",
  "CS"
)

n82 = N + Task(
  "Maintain/ Implement PHL Services",
  "CS"
)

n83 = N + SoftGoal(
  "*Increase Number of Services",
  "CS"
)

n84 = N + SoftGoal(
  "Efficient Services",
  "CS"
)

n85 = N + SoftGoal(
  "Available [Services]",
  "CS"
)

n86 = N + Task(
  "Acquire Funds",
  "CS"
)

n87 = N + SoftGoal(
  "Increased SA Resources",
  "CS"
)

n88 = N + SoftGoal(
  "Trust [of Kids]",
  "CS"
)

n89 = N + SoftGoal(
  "Quality SA Services",
  "CS"
)

n90 = N + SoftGoal(
  "Reduce Misconceptions",
  "CS"
)

n91 = N + SoftGoal(
  "Sufficient Counselling Resource",
  "CS"
)

n92 = N + SoftGoal(
  "Increase Funding for Training",
  "CS"
)

n93 = N + SoftGoal(
  "Reduce Cost of Counselling HR",
  "CS"
)

n94 = N + SoftGoal(
  "Accountability of services",
  "CS"
)

n95 = N + HardGoal(
  "Research on Kids Be Acquired",
  "CS"
)

n96 = N + SoftGoal(
  "*High Quality Counselling",
  "CS"
)

n97 = N + SoftGoal(
  "Avoid Liability Problems",
  "CS"
)

n98 = N + SoftGoal(
  "Responsible Usage[Sponsor Funds]",
  "CS"
)

n99 = N + SoftGoal(
  "Demonstrable Services",
  "CS"
)

n100 = N + SoftGoal(
  "Increase Volunteers",
  "CS"
)

n101 = N + SoftGoal(
  "Increase [Awareness]",
  "CS"
)

n102 = N + SoftGoal(
  "Avoid Over-Marketing Services",
  "CS"
)

n103 = N + SoftGoal(
  "Positive [Reputation of CS]",
  "CS"
)

n104 = N + SoftGoal(
  "Match Fundraising Targets",
  "CS"
)

n105 = N + SoftGoal(
  "Follow Highest Ethical Guidelines",
  "CS"
)

n106 = N + SoftGoal(
  "Credibility [CS Brand]",
  "CS"
)

n107 = N + SoftGoal(
  "Long Term Funding",
  "CS"
)

n108 = N + Task(
  "Provide Information to General Public",
  "CS"
)

n109 = N + HardGoal(
  "Services Be Free",
  "Parents, Kids & Youth"
)

n110 = N + HardGoal(
  "Collaborate with Not for Profit Partners on Services",
  "CS"
)

n111 = N + HardGoal(
  "Be Involved in Not for Profit Partners Events",
  "CS"
)

n112 = N + SoftGoal(
  "Help Kids",
  "CS"
)

n113 = N + SoftGoal(
  "Help Parents",
  "CS"
)

n114 = N + SoftGoal(
  "*Help As Many Kids as Possible",
  "CS"
)

n115 = N + SoftGoal(
  "Ability to Move Forward",
  "CS"
)

n116 = N + SoftGoal(
  "Sustainable Services",
  "CS"
)

n117 = N + SoftGoal(
  "Externally Unique[Services]",
  "CS"
)

n118 = N + SoftGoal(
  "Avoid Scandal",
  "CS"
)

n119 = N + SoftGoal(
  "Positive Internal Opinion",
  "CS"
)

n120 = N + SoftGoal(
  "Increase Funds",
  "CS"
)

n121 = N + SoftGoal(
  "Avoid Travel Spending",
  "CS"
)

n122 = N + SoftGoal(
  "Avoid Entertainment Spending",
  "CS"
)

n123 = N + SoftGoal(
  "Accessibility of Services",
  "CS"
)

n124 = N + SoftGoal(
  "Reduce Cost",
  "CS"
)

n125 = N + SoftGoal(
  "Safety Kids",
  "CS"
)

n126 = N + SoftGoal(
  "Increase Call/Web Volumes",
  "CS"
)

n127 = N + SoftGoal(
  "Find Needs and Wants of Kids",
  "CS"
)

n128 = N + Task(
  "Provide Resources",
  "CS"
)

n129 = N + SoftGoal(
  "Avoid Internal Duplication of Services",
  "CS"
)

n130 = N + Task(
  "Provide IT Resources",
  "CS"
)

n131 = N + Task(
  "Provide Service Resources",
  "CS"
)

n132 = N + Task(
  "Provide Resources to Regional Offices",
  "CS"
)

n133 = N + Task(
  "Provide Counselling Resources",
  "CS"
)

n134 = N + SoftGoal(
  "Service is National",
  "CS"
)


# EDGES

e1 = E + Dep(
  source = n63,
  target = n1
)

e2 = E + Dep(
  source = n65,
  target = n3
)

e3 = E + Dep(
  source = n130,
  target = n4
)

e4 = E + Dep(
  source = n70,
  target = n9
)

e5 = E + Dep(
  source = n76,
  target = n15
)

e6 = E + Dep(
  source = n131,
  target = n25
)

e7 = E + Dep(
  source = n132,
  target = n26
)

e8 = E + Dep(
  source = n91,
  target = n35
)

e9 = E + Dep(
  source = n92,
  target = n36
)

e10 = E + Dep(
  source = n133,
  target = n33
)

e11 = E + Dep(
  source = n73,
  target = n44
)

e12 = E + Dep(
  source = n98,
  target = n45
)

e13 = E + Dep(
  source = n99,
  target = n50
)

e14 = E + Dep(
  source = n100,
  target = n51
)

e15 = E + Dep(
  source = n94,
  target = n49
)

e16 = E + Dep(
  source = n103,
  target = n54
)

e17 = E + Dep(
  source = n105,
  target = n56
)

e18 = E + Dep(
  source = n106,
  target = n57
)

e19 = E + Dep(
  source = n108,
  target = n59
)

e20 = E + Dep(
  source = n109,
  target = n60
)

e21 = E + Dep(
  source = n111,
  target = n62
)

e22 = E + Dep(
  source = n2,
  target = n64
)

e23 = E + Dep(
  source = n5,
  target = n66
)

e24 = E + Dep(
  source = n6,
  target = n67
)

e25 = E + Dep(
  source = n7,
  target = n68
)

e26 = E + Help(
  source = n64,
  target = n68
)

e27 = E + Help(
  source = n117,
  target = n68
)

e28 = E + Dep(
  source = n8,
  target = n69
)

e29 = E + Help(
  source = n127,
  target = n69
)

e30 = E + Help(
  source = n79,
  target = n69
)

e31 = E + Help(
  source = n80,
  target = n69
)

e32 = E + Dep(
  source = n10,
  target = n71
)

e33 = E + Help(
  source = n74,
  target = n71
)

e34 = E + Dep(
  source = n11,
  target = n72
)

e35 = E + Dep(
  source = n12,
  target = n73
)

e36 = E + Dep(
  source = n13,
  target = n74
)

e37 = E + Dep(
  source = n14,
  target = n75
)

e38 = E + Dep(
  source = n16,
  target = n77
)

e39 = E + Help(
  source = n127,
  target = n77
)

e40 = E + Dep(
  source = n17,
  target = n78
)

e41 = E + Help(
  source = n77,
  target = n78
)

e42 = E + Help(
  source = n117,
  target = n78
)

e43 = E + Help(
  source = n96,
  target = n78
)

e44 = E + Help(
  source = n90,
  target = n78
)

e45 = E + Dep(
  source = n18,
  target = n79
)

e46 = E + Dep(
  source = n19,
  target = n80
)

e47 = E + Dep(
  source = n20,
  target = n81
)

e48 = E + Dep(
  source = n21,
  target = n82
)

e49 = E + Dep(
  source = n22,
  target = n83
)

e50 = E + Dep(
  source = n23,
  target = n84
)

e51 = E + Dep(
  source = n24,
  target = n85
)

e52 = E + Dep(
  source = n28,
  target = n87
)

e53 = E + Dep(
  source = n29,
  target = n88
)

e54 = E + Dep(
  source = n30,
  target = n89
)

e55 = E + Dep(
  source = n31,
  target = n90
)

e56 = E + Hurt(
  source = n126,
  target = n91
)

e57 = E + Help(
  source = n120,
  target = n91
)

e58 = E + Dep(
  source = n37,
  target = n93
)

e59 = E + Dep(
  source = n38,
  target = n94
)

e60 = E + Dep(
  source = n40,
  target = n95
)

e61 = E + Dep(
  source = n41,
  target = n96
)

e62 = E + Dep(
  source = n43,
  target = n97
)

e63 = E + Help(
  source = n121,
  target = n98
)

e64 = E + Help(
  source = n122,
  target = n98
)

e65 = E + Help(
  source = n71,
  target = n99
)

e66 = E + Help(
  source = n126,
  target = n99
)

e67 = E + Help(
  source = n80,
  target = n99
)

e68 = E + Help(
  source = n118,
  target = n100
)

e69 = E + Help(
  source = n70,
  target = n100
)

e70 = E + Help(
  source = n106,
  target = n100
)

e71 = E + Help(
  source = n103,
  target = n100
)

e72 = E + Help(
  source = n108,
  target = n101
)

e73 = E + Help(
  source = n111,
  target = n101
)

e74 = E + Dep(
  source = n54,
  target = n102
)

e75 = E + Help(
  source = n96,
  target = n103
)

e76 = E + Help(
  source = n95,
  target = n103
)

e77 = E + Help(
  source = n94,
  target = n103
)

e78 = E + Help(
  source = n118,
  target = n103
)

e79 = E + Help(
  source = n105,
  target = n103
)

e80 = E + Help(
  source = n107,
  target = n103
)

e81 = E + Help(
  source = n71,
  target = n103
)

e82 = E + Help(
  source = n123,
  target = n103
)

e83 = E + Dep(
  source = n55,
  target = n104
)

e84 = E + Help(
  source = n63,
  target = n105
)

e85 = E + Help(
  source = n105,
  target = n106
)

e86 = E + Help(
  source = n103,
  target = n106
)

e87 = E + Help(
  source = n118,
  target = n106
)

e88 = E + Help(
  source = n107,
  target = n106
)

e89 = E + Help(
  source = n108,
  target = n106
)

e90 = E + Help(
  source = n63,
  target = n106
)

e91 = E + Dep(
  source = n58,
  target = n107
)

e92 = E + Dep(
  source = n47,
  target = n108
)

e93 = E + Dep(
  source = n48,
  target = n108
)

e94 = E + Dep(
  source = n61,
  target = n110
)

e95 = E + Help(
  source = n111,
  target = n112
)

e96 = E + Help(
  source = n64,
  target = n112
)

e97 = E + Help(
  source = n113,
  target = n112
)

e98 = E + Help(
  source = n67,
  target = n112
)

e99 = E + Help(
  source = n69,
  target = n112
)

e100 = E + Help(
  source = n70,
  target = n112
)

e101 = E + Help(
  source = n125,
  target = n112
)

e102 = E + Help(
  source = n77,
  target = n112
)

e103 = E + Help(
  source = n79,
  target = n112
)

e104 = E + Help(
  source = n88,
  target = n112
)

e105 = E + Help(
  source = n116,
  target = n112
)

e106 = E + Help(
  source = n96,
  target = n112
)

e107 = E + Help(
  source = n90,
  target = n112
)

e108 = E + Help(
  source = n82,
  target = n113
)

e109 = E + Help(
  source = n64,
  target = n114
)

e110 = E + Help(
  source = n134,
  target = n114
)

e111 = E + Help(
  source = n70,
  target = n114
)

e112 = E + Help(
  source = n72,
  target = n114
)

e113 = E + Help(
  source = n78,
  target = n114
)

e114 = E + Help(
  source = n123,
  target = n114
)

e115 = E + Help(
  source = n84,
  target = n114
)

e116 = E + Help(
  source = n85,
  target = n114
)

e117 = E + Help(
  source = n89,
  target = n114
)

e118 = E + Help(
  source = n101,
  target = n114
)

e119 = E + Help(
  source = n132,
  target = n134
)

e120 = E + Help(
  source = n64,
  target = n115
)

e121 = E + Help(
  source = n68,
  target = n115
)

e122 = E + Help(
  source = n83,
  target = n115
)

e123 = E + Help(
  source = n120,
  target = n115
)

e124 = E + Help(
  source = n116,
  target = n115
)

e125 = E + Help(
  source = n117,
  target = n116
)

e126 = E + Help(
  source = n77,
  target = n116
)

e127 = E + Hurt(
  source = n83,
  target = n116
)

e128 = E + Help(
  source = n84,
  target = n116
)

e129 = E + Help(
  source = n124,
  target = n116
)

e130 = E + Help(
  source = n102,
  target = n116
)

e131 = E + Help(
  source = n104,
  target = n116
)

e132 = E + Help(
  source = n107,
  target = n116
)

e133 = E + Help(
  source = n110,
  target = n117
)

e134 = E + Help(
  source = n85,
  target = n117
)

e135 = E + Help(
  source = n105,
  target = n118
)

e136 = E + Help(
  source = n94,
  target = n118
)

e137 = E + Help(
  source = n97,
  target = n118
)

e138 = E + Help(
  source = n98,
  target = n118
)

e139 = E + Help(
  source = n117,
  target = n119
)

e140 = E + Help(
  source = n118,
  target = n119
)

e141 = E + Help(
  source = n126,
  target = n119
)

e142 = E + Hurt(
  source = n108,
  target = n120
)

e143 = E + Help(
  source = n104,
  target = n120
)

e144 = E + Help(
  source = n118,
  target = n120
)

e145 = E + Help(
  source = n124,
  target = n120
)

e146 = E + Help(
  source = n83,
  target = n120
)

e147 = E + Help(
  source = n86,
  target = n120
)

e148 = E + Help(
  source = n80,
  target = n123
)

e149 = E + Help(
  source = n81,
  target = n123
)

e150 = E + Hurt(
  source = n65,
  target = n124
)

e151 = E + Help(
  source = n66,
  target = n124
)

e152 = E + Hurt(
  source = n76,
  target = n124
)

e153 = E + Help(
  source = n129,
  target = n124
)

e154 = E + Hurt(
  source = n83,
  target = n124
)

e155 = E + Help(
  source = n84,
  target = n124
)

e156 = E + Hurt(
  source = n128,
  target = n124
)

e157 = E + Hurt(
  source = n87,
  target = n124
)

e158 = E + Hurt(
  source = n91,
  target = n124
)

e159 = E + Hurt(
  source = n92,
  target = n124
)

e160 = E + Help(
  source = n93,
  target = n124
)

e161 = E + Help(
  source = n73,
  target = n125
)

e162 = E + Help(
  source = n75,
  target = n125
)

e163 = E + Help(
  source = n101,
  target = n126
)

e164 = E + Hurt(
  source = n102,
  target = n126
)

e165 = E + Help(
  source = n103,
  target = n126
)

e166 = E + Help(
  source = n77,
  target = n126
)

e167 = E + Help(
  source = n88,
  target = n126
)

e168 = E + Help(
  source = n90,
  target = n126
)

e169 = E + Help(
  source = n96,
  target = n126
)

e170 = E + Help(
  source = n95,
  target = n127
)

e171 = E + Or(
  source = n130,
  target = n128
)

e172 = E + Or(
  source = n131,
  target = n128
)

e173 = E + Or(
  source = n132,
  target = n128
)

e174 = E + Or(
  source = n133,
  target = n128
)

e175 = E + Hurt(
  source = n80,
  target = n129
)

e176 = E + Or(
  source = n86,
  target = n130
)

e177 = E + Or(
  source = n86,
  target = n131
)

e178 = E + Or(
  source = n86,
  target = n132
)

e179 = E + Or(
  source = n86,
  target = n133
)

graph = Graph(name="CSAgentSR", nodes=N.all, edges=E.all)
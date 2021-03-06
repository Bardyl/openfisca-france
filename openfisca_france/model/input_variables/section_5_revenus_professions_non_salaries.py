# -*- coding: utf-8 -*-


# OpenFisca -- A versatile microsimulation software
# By: OpenFisca Team <contact@openfisca.fr>
#
# Copyright (C) 2011, 2012, 2013, 2014 OpenFisca Team
# https://github.com/openfisca
#
# This file is part of OpenFisca.
#
# OpenFisca is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# OpenFisca is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import collections
import datetime

from openfisca_core.columns import BoolCol, IntCol

from base import QUIFOY, build_column_couple


column_by_name = collections.OrderedDict((

    build_column_couple('f5qm', IntCol(entity = 'ind',
                    label = u"Agents généraux d’assurances: indemnités de cessation d’activité",
                    val_type = "monetary",
                    cerfa_field = {QUIFOY['vous']: u"5QM",
                                   QUIFOY['conj']: u"5RM",
                                   })),  # (f5qm, f5rm )

    # Revenus des professions non salariées
    build_column_couple('ppe_du_ns', IntCol(entity = 'ind', label = u"Prime pour l'emploi des non-salariés: nombre de jours travaillés dans l'année",
                         cerfa_field = {QUIFOY['vous']: u"5NV",
                                        QUIFOY['conj']: u"5OV",
                                        QUIFOY['pac1']: u"5PV",
                                   })),  # (f5nv, f5ov, f5pv)

    build_column_couple('ppe_tp_ns', BoolCol(entity = 'ind', label = u"Prime pour l'emploi des non-salariés: indicateur de travail à temps plein sur l'année entière",
                          cerfa_field = {QUIFOY['vous']: u"5NW",
                                         QUIFOY['conj']: u"5OW",
                                         QUIFOY['pac1']: u"5PW",
                                         })),  # (f5nw, f5ow, f5pw)

    build_column_couple('frag_exon', IntCol(entity = 'ind', label = u"Revenus agricoles exonérés (régime du forfait)", val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5HN",
                                        QUIFOY['conj']: u"5IN",
                                        QUIFOY['pac1']: u"5JN", })),  # (f5hn, f5in, f5jn)),

    build_column_couple('frag_impo', IntCol(entity = 'ind',
                         label = u"Revenus agricoles imposables (régime du forfait)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5HO",
                                        QUIFOY['conj']: u"5IO",
                                        QUIFOY['pac1']: u"5JO", })),  # (f5ho, f5io, f5jo)),

    build_column_couple('arag_exon', IntCol(entity = 'ind',
                         label = u"Revenus agricoles exonérés yc plus-values (Régime du bénéfice réel, revenus bénéficiant de l'abattement CGA ou viseur), activités exercées en Corse",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5HB",
                                        QUIFOY['conj']: u"5IB",
                                        QUIFOY['pac1']: u"5JB", })),  # (f5hb, f5ib, f5jb)),

    build_column_couple('arag_impg', IntCol(entity = 'ind',
                         label = u"Revenus agricoles imposables, cas général moyenne triennale (Régime du bénéfice réel, revenus bénéficiant de l'abattement CGA ou viseur)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5HC",
                                        QUIFOY['conj']: u"5IC",
                                        QUIFOY['pac1']: u"5JC", })),  # (f5hc, f5ic, f5jc)),

    build_column_couple('arag_defi', IntCol(entity = 'ind',
                         label = u"Déficits agricoles (Régime du bénéfice réel, revenus bénéficiant de l'abattement CGA ou viseur)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5HF",
                                        QUIFOY['conj']: u"5IF",
                                        QUIFOY['pac1']: u"5JF", })),  # (f5hf, f5if, f5jf)),

    build_column_couple('nrag_exon', IntCol(entity = 'ind',
                         label = u"Revenus agricoles exonérés yc plus-values (Régime du bénéfice réel, revenus ne bénéficiant pas de l'abattement CGA ou viseur), activités exercées en Corse",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5HH",
                                        QUIFOY['conj']: u"5IH",
                                        QUIFOY['pac1']: u"5JH", })),  # (f5hh, f5ih, f5jh)),

    build_column_couple('nrag_impg', IntCol(entity = 'ind',
                         label = u"Revenus agricoles imposables, cas général moyenne triennale (Régime du bénéfice réel, revenus ne bénéficiant pas de l'abattement CGA ou viseur)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5HI",
                                        QUIFOY['conj']: u"5II",
                                        QUIFOY['pac1']: u"5JI", })),  # (f5hi, f5ii, f5ji)),

    build_column_couple('nrag_defi', IntCol(entity = 'ind',
                         label = u"Déficits agricoles (Régime du bénéfice réel, revenus ne bénéficiant pas de l'abattement CGA ou viseur)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5HL",
                                        QUIFOY['conj']: u"5IL",
                                        QUIFOY['pac1']: u"5JL", })),  # (f5hl, f5il, f5jl)),

    build_column_couple('nrag_ajag', IntCol(entity = 'ind',
                         label = u"Jeunes agriculteurs, Abattement de 50% ou 100% (Régime du bénéfice réel, revenus bénéficiant de l'abattement CGA ou viseur)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5HM",
                                        QUIFOY['conj']: u"5IM",
                                        QUIFOY['pac1']: u"5JM", })),  # (f5hm, f5im, f5jm)),

    # Autoentrepreneur
    build_column_couple('ebic_impv', IntCol(entity = 'ind',
                         label = u"Revenus industriels et commerciaux professionnels imposables: vente de marchandises et assimilées (régime auto-entrepreneur)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5TA",
                                        QUIFOY['conj']: u"5UA",
                                        QUIFOY['pac1']: u"5VA", })),  # (f5ta, f5ua, f5va)),

    build_column_couple('ebic_imps', IntCol(entity = 'ind',
                         label = u"Revenus industriels et commerciaux professionnels imposables: prestations de services et locations meublées (régime auto-entrepreneur)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5TB",
                                        QUIFOY['conj']: u"5UB",
                                        QUIFOY['pac1']: u"5VB", })),  # (f5tb, f5ub, f5vb)),

    build_column_couple('ebnc_impo', IntCol(entity = 'ind',
                         label = u"Revenus non commerciaux imposables (régime auto-entrepreneur)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5TE",
                                        QUIFOY['conj']: u"5UE",
                                        QUIFOY['pac1']: u"5VE", })),  # (f5te, f5ue, f5ve)),

    build_column_couple('mbic_exon', IntCol(entity = 'ind',
                         label = u"Revenus industriels et commerciaux professionnels nets exonérés (régime micro entreprise)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5KN",
                                        QUIFOY['conj']: u"5LN",
                                        QUIFOY['pac1']: u"5MN", })),  # (f5kn, f5ln, f5mn)),

    build_column_couple('abic_exon', IntCol(entity = 'ind',
                         label = u"Revenus industriels et commerciaux nets exonérés yc plus-values avec CGA ou viseur (régime du bénéfice réel)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5KB",
                                        QUIFOY['conj']: u"5LB",
                                        QUIFOY['pac1']: u"5MB", })),  # (f5kb, f5lb, f5mb)),

    build_column_couple('nbic_exon', IntCol(entity = 'ind',
                         label = u"Revenus industriels et commerciaux nets exonérés yc plus-values sans CGA (régime du bénéfice réel)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5KH",
                                        QUIFOY['conj']: u"5LH",
                                        QUIFOY['pac1']: u"5MH", })),  # (f5kh, f5lh, f5mh)),

    build_column_couple('mbic_impv', IntCol(entity = 'ind',
                         label = u"Revenus industriels et commerciaux professionnels imposables: vente de marchandises (régime micro entreprise)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5KO",
                                        QUIFOY['conj']: u"5LO",
                                        QUIFOY['pac1']: u"5MO", })),  # (f5ko, f5lo, f5mo)),

    build_column_couple('mbic_imps', IntCol(entity = 'ind',
                         label = u"Revenus industriels et commerciaux professionnels imposables: prestations de services et locations meublées (régime micro entreprise)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5KP",
                                        QUIFOY['conj']: u"5LP",
                                        QUIFOY['pac1']: u"5MP", })),  # (f5kp, f5lp, f5mp)),

    build_column_couple('abic_impn', IntCol(entity = 'ind',
                         label = u"Revenus industriels et commerciaux imposables: régime normal ou simplifié avec CGA ou viseur (régime du bénéfice réel)",
                          val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5KC",
                                        QUIFOY['conj']: u"5LC",
                                        QUIFOY['pac1']: u"5MC", })),  # (f5kc, f5lc, f5mc)),

    build_column_couple('abic_imps', IntCol(entity = 'ind',
                         label = u"Revenus industriels et commerciaux imposables: régime simplifié avec CGA ou viseur (régime du bénéfice réel)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5KD",
                                        QUIFOY['conj']: u"5LD",
                                        QUIFOY['pac1']: u"5MD", },
                         end = datetime.date(2012, 12, 1))),  # (f5kd, f5ld, f5md)),
                                                              # TODO: vérifier date fin

    build_column_couple('nbic_impn', IntCol(entity = 'ind',
                         label = u"Revenus industriels et commerciaux imposables: régime normal ou simplifié sans CGA (régime du bénéfice réel)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5KI",
                                        QUIFOY['conj']: u"5LI",
                                        QUIFOY['pac1']: u"5MI", }
                         )),  # (f5ki, f5li, f5mi)),

# """
# réutilisation cases 2013
# """
    build_column_couple('nbic_imps', IntCol(entity = 'ind',
                         label = u"Revenus industriels et commerciaux imposables: régime simplifié sans CGA (régime du bénéfice réel)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5KJ",
                                        QUIFOY['conj']: u"5LJ",
                                        QUIFOY['pac1']: u"5MJ", },
                         end = datetime.date(2012, 12, 1))),  # (f5kj, f5lj, f5mj)),
                                                              # TODO: vérifier date fin
    build_column_couple('nbic_mvct', IntCol(entity = 'ind',
                         label = u"Revenus industriels et commerciaux moins-values nettes à court terme",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5KJ",
                                        QUIFOY['conj']: u"5LJ",
                                        QUIFOY['pac1']: u"5MJ", },
                         start = datetime.date(2013, 1, 1))),  # (f5kj, f5lj, f5mj)),
                                                              # vérifier date début #####à intégrer dans OF#######

    build_column_couple('abic_defn', IntCol(entity = 'ind',
                         label = u"Déficits industriels et commerciaux: régime normal ou simplifié avec CGA ou viseur (régime du bénéfice réel)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5KF",
                                        QUIFOY['conj']: u"5LF",
                                        QUIFOY['pac1']: u"5MF", })),  # (f5kf, f5lf, f5mf)),

    build_column_couple('abic_defs', IntCol(entity = 'ind',
                         label = u"Déficits industriels et commerciaux: simplifié avec CGA ou viseur (régime du bénéfice réel)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5KG",
                                        QUIFOY['conj']: u"5LG",
                                        QUIFOY['pac1']: u"5MG", },
                         end = datetime.date(2012, 12, 1))),  # (f5kg, f5lg, f5mg)),
                                                              # vérif <=2012

    build_column_couple('nbic_defn', IntCol(entity = 'ind',
                         label = u"Déficits industriels et commerciaux: régime normal ou simplifié sans CGA (régime du bénéfice réel)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5KL",
                                        QUIFOY['conj']: u"5LL",
                                        QUIFOY['pac1']: u"5ML", })),  # (f5kl, f5ll, f5ml)),

    build_column_couple('nbic_defs', IntCol(entity = 'ind',
                         label = u"Locations déjà soumises aux prélèvements sociaux sans CGA (régime du bénéfice réel)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5KL",
                                        QUIFOY['conj']: u"5LM",
                                        QUIFOY['pac1']: u"5MM", })),  # (f5km, f5lm, f5mm)),

    build_column_couple('nbic_apch', IntCol(entity = 'ind',
                         label = u"Artisans pêcheurs : abattement 50% avec CGA ou viseur (régime du bénéfice réel)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5KS",
                                        QUIFOY['conj']: u"5LS",
                                        QUIFOY['pac1']: u"5MS", })),  # (f5ks, f5ls, f5ms)),

    build_column_couple('macc_exon', IntCol(entity = 'ind',
                         label = u"Revenus industriels et commerciaux non professionnels nets exonérés (régime micro entreprise)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5NN",
                                        QUIFOY['conj']: u"5ON",
                                        QUIFOY['pac1']: u"5PN", })),  # (f5nn, f5on, f5pn)),

    build_column_couple('aacc_exon', IntCol(entity = 'ind',
                         label = u"Revenus industriels et commerciaux non professionnels exonérés yc plus-values avec CGA ou viseur (régime du bénéfice réel)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5NB",
                                        QUIFOY['conj']: u"5OB",
                                        QUIFOY['pac1']: u"5PB", })),  # (f5nb, f5ob, f5pb)),

    build_column_couple('nacc_exon', IntCol(entity = 'ind',
                         label = u"Revenus industriels et commerciaux non professionnels exonérés yc plus-values sans CGA (régime du bénéfice réel)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5NH",
                                        QUIFOY['conj']: u"5OH",
                                        QUIFOY['pac1']: u"5PH", })),  # (f5nh, f5oh, f5ph)),

    build_column_couple('macc_impv', IntCol(entity = 'ind',
                         label = u"Revenus industriels et commerciaux non professionnels imposables: vente de marchandises et assimilées (régime micro entreprise)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5NO",
                                        QUIFOY['conj']: u"5OO",
                                        QUIFOY['pac1']: u"5PO", })),  # (f5no, f5oo, f5po)),

    build_column_couple('macc_imps', IntCol(entity = 'ind',
                         label = u"Revenus industriels et commerciaux non professionnels imposables: prestations de services (régime micro entreprise)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5NP",
                                        QUIFOY['conj']: u"5OP",
                                        QUIFOY['pac1']: u"5PP", })),  # (f5np, f5op, f5pp)),

    build_column_couple('aacc_impn', IntCol(entity = 'ind',
                         label = u"Revenus industriels et commerciaux non professionnels imposables: régime normal ou simplifié avec CGA ou viseur (régime du bénéfice réel)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5NC",
                                        QUIFOY['conj']: u"5OC",
                                        QUIFOY['pac1']: u"5PC", })),  # (f5nc, f5oc, f5pc)),

    build_column_couple('aacc_imps', IntCol(entity = 'ind',
                         label = u"Locations meublées non professionnelles (régime micro entreprise)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5ND",
                                        QUIFOY['conj']: u"5OD",
                                        QUIFOY['pac1']: u"5PD", })),  # (f5nd, f5od, f5pd)),

    build_column_couple('aacc_defn', IntCol(entity = 'ind',
                         label = u"Déficits industriels et commerciaux non professionnels: régime normal ou simplifié avec CGA ou viseur (régime du bénéfice réel)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5NF",
                                        QUIFOY['conj']: u"5OF",
                                        QUIFOY['pac1']: u"5PF", })),  # (f5nf, f5of, f5pf)),

    build_column_couple('aacc_defs', IntCol(entity = 'ind',
                         label = u"Location de gîtes ruraux, chambres d'hôtes et meublés de tourisme (régime micro entreprise)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5NG",
                                        QUIFOY['conj']: u"5OG",
                                        QUIFOY['pac1']: u"5PG", })),  # (f5ng, f5og, f5pg)),

    build_column_couple('nacc_impn', IntCol(entity = 'ind',
                         label = u"Revenus industriels et commerciaux non professionnels imposables: régime normal ou simplifié sans CGA (régime du bénéfice réel)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5NI",
                                        QUIFOY['conj']: u"5OI",
                                        QUIFOY['pac1']: u"5PI", })),  # (f5ni, f5oi, f5pi)),

    build_column_couple('nacc_imps', IntCol(entity = 'ind',
                         label = u"Locations meublées non professionnelles: Locations déjà soumises aux prélèvements sociaux (régime micro entreprise)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5NJ",
                                        QUIFOY['conj']: u"5OJ",
                                        QUIFOY['pac1']: u"5PJ", })),  # (f5nj, f5oj, f5pj)),

    build_column_couple('nacc_defn', IntCol(entity = 'ind',
                         label = u"Déficits industriels et commerciaux non professionnels: régime normal ou simplifié sans CGA (régime du bénéfice réel)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5NL",
                                        QUIFOY['conj']: u"5OL",
                                        QUIFOY['pac1']: u"5PL", })),  # (f5nl, f5ol, f5pl)),

    build_column_couple('nacc_defs', IntCol(entity = 'ind',
                         label = u"Locations meublées non professionnelles: Locations déjà soumises aux prélèvements sociaux avec CGA ou viseur (régime du bénéfice réel)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5NM",
                                        QUIFOY['conj']: u"5OM",
                                        QUIFOY['pac1']: u"5PM", })),  # (f5nm, f5om, f5pm)),

    build_column_couple('mncn_impo', IntCol(entity = 'ind',
                         label = u"Revenus non commerciaux non professionnels imposables (régime déclaratif spécial ou micro BNC)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5KU",
                                        QUIFOY['conj']: u"5LU",
                                        QUIFOY['pac1']: u"5MU", })),  # (f5ku, f5lu, f5mu)),

    build_column_couple('cncn_bene', IntCol(entity = 'ind',
                         label = u"Revenus non commerciaux non professionnels imposables sans AA (régime de la déclaration controlée)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5SN",
                                        QUIFOY['conj']: u"5NS",
                                        QUIFOY['pac1']: u"5OS", })),  # (f5sn, f5ns, f5os)),

    build_column_couple('cncn_defi', IntCol(entity = 'ind',
                         label = u"Déficits non commerciaux non professionnels sans AA (régime de la déclaration controlée)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5SP",
                                        QUIFOY['conj']: u"5NU",
                                        QUIFOY['pac1']: u"5OU", })),  # (f5sp, f5nu, f5ou, f5sr)),
                                                                      # pas de f5sr en 2013

    build_column_couple('mbnc_exon', IntCol(entity = 'ind',
                         label = u"Revenus non commerciaux professionnels nets exonérés (régime déclaratif spécial ou micro BNC)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5HP",
                                        QUIFOY['conj']: u"5IP",
                                        QUIFOY['pac1']: u"5JP", })),  # (f5hp, f5ip, f5jp)),

    build_column_couple('abnc_exon', IntCol(entity = 'ind',
                         label = u"Revenus non commerciaux professionnels exonérés (yc compris plus-values) (régime de la déclaration controlée, revenus bénéficiant de l'abattement association agrée ou viseur)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5QB",
                                        QUIFOY['conj']: u"5RB",
                                        QUIFOY['pac1']: u"5SB", })),  # (f5qb, f5rb, f5sb)),

    build_column_couple('nbnc_exon', IntCol(entity = 'ind',
                         label = u"Revenus non commerciaux professionnels exonérés (yc compris plus-values) (régime de la déclaration controlée, revenus ne bénéficiant pas de l'abattement association agrée)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5QH",
                                        QUIFOY['conj']: u"5RH",
                                        QUIFOY['pac1']: u"5SH", })),  # (f5qh, f5rh, f5sh)),

    build_column_couple('mbnc_impo', IntCol(entity = 'ind',
                         label = u"Revenus non commerciaux professionnels imposables (régime déclaratif spécial ou micro BNC)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5HQ",
                                        QUIFOY['conj']: u"5IQ",
                                        QUIFOY['pac1']: u"5JQ", })),  # (f5hq, f5iq, f5jq)),

    build_column_couple('abnc_impo', IntCol(entity = 'ind',
                         label = u"Revenus non commerciaux professionnels imposables (régime de la déclaration controlée, revenus bénéficiant de l'abattement association agrée ou viseur)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5QC",
                                        QUIFOY['conj']: u"5RC",
                                        QUIFOY['pac1']: u"5SC", })),  # (f5qc, f5rc, f5sc)),

    build_column_couple('abnc_defi', IntCol(entity = 'ind',
                         label = u"Déficits non commerciaux professionnels (régime de la déclaration controlée, revenus bénéficiant de l'abattement association agrée ou viseur)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5QE",
                                        QUIFOY['conj']: u"5RE",
                                        QUIFOY['pac1']: u"5SE", })),  # (f5qe, f5re, f5se)),

    build_column_couple('nbnc_impo', IntCol(entity = 'ind',
                         label = u"Revenus non commerciaux professionnels imposables (régime de la déclaration controlée, revenus ne bénéficiant pas de l'abattement association agrée)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5QI",
                                        QUIFOY['conj']: u"5RI",
                                        QUIFOY['pac1']: u"5SI", })),  # (f5qi, f5ri, f5si)),

    build_column_couple('nbnc_defi', IntCol(entity = 'ind',
                         label = u"Déficits non commerciaux professionnels (régime de la déclaration controlée, revenus ne bénéficiant pas de l'abattement association agrée)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5QK",
                                        QUIFOY['conj']: u"5RK",
                                        QUIFOY['pac1']: u"5SK", })),  # (f5qk, f5rk, f5sk)),

    build_column_couple('mbic_mvct', IntCol(entity = 'foy',
                         label = u"Moins-values industrielles et commerciales nettes à court terme du foyer (régime micro entreprise)",
                         val_type = "monetary",
                         cerfa_field = u'5HU',
                         end = datetime.date(2012, 12, 1))),  # (f5hu)),
                                                              # vérif <=2012

    build_column_couple('macc_mvct', IntCol(entity = 'foy', label = u"Moins-values industrielles et commerciales non professionnelles nettes à court terme du foyer (régime micro entreprise)",
                         val_type = "monetary",
                         cerfa_field = u'5IU')),  # (f5iu)),

    build_column_couple('mncn_mvct', IntCol(entity = 'foy',
                         label = u"Moins-values non commerciales non professionnelles nettes à court terme du foyer (régime déclaratif spécial ou micro BNC)",
                         val_type = "monetary",
                         cerfa_field = u'JU')),  # (f5ju)),

    build_column_couple('mbnc_mvct', IntCol(entity = 'foy', label = u"Moins-values non commerciales professionnelles nettes à court terme (régime déclaratif spécial ou micro BNC)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5KZ",
                                        QUIFOY['conj']: u"5LZ",
                                        QUIFOY['pac1']: u"5MZ", })),  # (f5kz, f5lz , f5mz), f5lz , f5mz sont présentent en 2013
                                                                      # TODO: intégrer f5lz , f5mz à OF

    build_column_couple('frag_pvct', IntCol(entity = 'ind',
                         label = u"Plus-values agricoles  à court terme (régime du forfait)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5HW",
                                        QUIFOY['conj']: u"5IW",
                                        QUIFOY['pac1']: u"5JW", })),  # (f5hw, f5iw, f5jw)),

    build_column_couple('mbic_pvct', IntCol(entity = 'ind',
                         label = u"Plus-values industrielles et commerciales professionnels imposables: plus-values nettes à court terme (régime micro entreprise)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5KX",
                                        QUIFOY['conj']: u"5LX",
                                        QUIFOY['pac1']: u"5MX", })),  # (f5kx, f5lx, f5mx)),

    build_column_couple('macc_pvct', IntCol(entity = 'ind',
                         label = u"Plus-values industrielles et commerciales non professionnelles imposables: plus-values nettes à court terme (régime micro entreprise)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5NX",
                                        QUIFOY['conj']: u"5OX",
                                        QUIFOY['pac1']: u"5PX", })),  # (f5nx, f5ox, f5px)),

    build_column_couple('mbnc_pvct', IntCol(entity = 'ind',
                         label = u"Plus-values non commerciales professionnelles imposables et Plus-values nettes à court terme (régime déclaratif spécial ou micro BNC)",
                          val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5HV",
                                        QUIFOY['conj']: u"5IV",
                                        QUIFOY['pac1']: u"5JV", })),  # (f5hv, f5iv, f5jv)),

    build_column_couple('mncn_pvct', IntCol(entity = 'ind',
                         label = u"Plus-values non commerciales non professionnelles imposables et plus-values nettes à court terme (régime déclaratif spécial ou micro BNC)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5KY",
                                        QUIFOY['conj']: u"5LY",
                                        QUIFOY['pac1']: u"5MY", })),  # (f5ky, f5ly, f5my)),

    build_column_couple('mbic_mvlt', IntCol(entity = 'ind',
                         label = u"Moins-values industrielles et commerciales professionnels à long terme (régime micro entreprise)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5KR",
                                        QUIFOY['conj']: u"5LR",
                                        QUIFOY['pac1']: u"5MR", })),  # (f5kr, f5lr, f5mr)),

    build_column_couple('macc_mvlt', IntCol(entity = 'ind',
                         label = u"Moins-values industrielles et commerciales non professionnelles à long terme (régime micro entreprise)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5NR",
                                        QUIFOY['conj']: u"5OR",
                                        QUIFOY['pac1']: u"5PR", })),  # (f5nr, f5or, f5pr)),

    build_column_couple('mncn_mvlt', IntCol(entity = 'ind',
                         label = u"Moins-values non commerciales non professionnelles à long terme (régime déclaratif spécial ou micro BNC)", val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5KW",
                                        QUIFOY['conj']: u"5LW",
                                        QUIFOY['pac1']: u"5MW", })),  # (f5kw, f5lw, f5mw)),

    build_column_couple('mbnc_mvlt', IntCol(entity = 'ind',
                         label = u"Moins-values non commerciales professionnelles à long terme (régime déclaratif spécial ou micro BNC)", val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5HS",
                                        QUIFOY['conj']: u"5IS",
                                        QUIFOY['pac1']: u"5JS", })),  # (f5hs, f5is, f5js)),

    build_column_couple('frag_pvce', IntCol(entity = 'ind',
                         label = u"Plus-values agricoles de cession taxables à 16% (régime du forfait)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5HX",
                                        QUIFOY['conj']: u"5IX",
                                        QUIFOY['pac1']: u"5JX", })),  # (f5hx, f5ix, f5jx)),

    build_column_couple('arag_pvce', IntCol(entity = 'ind',
                         label = u"Plus-values agricoles de cession taxables à 16% (Régime du bénéfice réel, revenus bénéficiant de l'abattement CGA ou viseur)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5HE",
                                        QUIFOY['conj']: u"5IE",
                                        QUIFOY['pac1']: u"5JE", })),  # (f5he, f5ie, f5je)),

    build_column_couple('nrag_pvce', IntCol(entity = 'ind',
                         label = u"Plus-values agricoles de cession taxables à 16% (Régime du bénéfice réel, revenus ne bénéficiant pas de l'abattement CGA ou viseur)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5HK",
                                        QUIFOY['conj']: u"5LK",
                                        QUIFOY['pac1']: u"5JK", },
                         end = datetime.date(2012, 12, 1))),  # TODO: vérif <=2012)),  # (f5hk, f5lk, f5jk)),

    build_column_couple('mbic_pvce', IntCol(entity = 'ind',
                         label = u"Plus-values industrielles et commerciales professionnelles imposables: plus-values de cession taxables à 16% (régime micro entreprise)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5KQ",
                                        QUIFOY['conj']: u"5LQ",
                                        QUIFOY['pac1']: u"5MQ", })),  # (f5kq, f5lq, f5mq)),

    build_column_couple('abic_pvce', IntCol(entity = 'ind',
                         label = u"Plus-values industrielles et commerciales de cession taxables à 16% avec CGA ou viseur (régime du bénéfice réel)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5KE",
                                        QUIFOY['conj']: u"5LE",
                                        QUIFOY['pac1']: u"5ME", })),  # (f5ke, f5le, f5me)),

    build_column_couple('nbic_pvce', IntCol(entity = 'ind',
                         label = u"Revenus non commerciaux non professionnels exonérés sans AA (régime de la déclaration controlée)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5IK",
                                        QUIFOY['conj']: u"5KK",
                                        QUIFOY['pac1']: u"5MK", })),  # (f5kk, f5ik, f5mk)),

    build_column_couple('macc_pvce', IntCol(entity = 'ind',
                         label = u"Plus-values industrielles et commerciales non professionnelles imposables: plus-values de cession taxables à 16% (régime micro entreprise)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5NQ",
                                        QUIFOY['conj']: u"5OQ",
                                        QUIFOY['pac1']: u"5PQ", })),  # (f5nq, f5oq, f5pq)),

    build_column_couple('aacc_pvce', IntCol(entity = 'ind',
                         label = u"Plus-values industrielles et commerciales non professionnelles de cession taxables à 16% avec CGA ou viseur (régime du bénéfice réel)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5NE",
                                        QUIFOY['conj']: u"5OE",
                                        QUIFOY['pac1']: u"5PE", })),  # (f5ne, f5oe, f5pe)),

    build_column_couple('nacc_pvce', IntCol(entity = 'ind',
                         label = u"Locations meublées non professionnelles: Revenus imposables sans CGA (régime du bénéfice réel)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5NK",
                                        QUIFOY['conj']: u"5OK",
                                        QUIFOY['pac1']: u"5PK", })),  # (f5nk, f5ok, f5pk)),

    build_column_couple('mncn_pvce', IntCol(entity = 'ind',
                         label = u"Plus-values non commerciales non professionnelles de cession taxables à 16% (régime déclaratif spécial ou micro BNC)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5KV",
                                        QUIFOY['conj']: u"5LV",
                                        QUIFOY['pac1']: u"5MV", })),  # (f5kv, f5lv, f5mv)),

    build_column_couple('cncn_pvce', IntCol(entity = 'ind',
                         label = u"Plus-values non commerciales non professionnelles taxables à 16% avec AA ou viseur (régime de la déclaration controlée)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5SO",
                                        QUIFOY['conj']: u"5NT",
                                        QUIFOY['pac1']: u"5OT", })),  # (f5so, f5nt, f5ot)),

    build_column_couple('mbnc_pvce', IntCol(entity = 'ind',
                         label = u"Plus-values non commerciales professionnelles de cession taxables à 16% (régime déclaratif spécial ou micro BNC)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5HR",
                                        QUIFOY['conj']: u"5IR",
                                        QUIFOY['pac1']: u"5JR", })),  # (f5hr, f5ir, f5jr)),

    build_column_couple('abnc_pvce', IntCol(entity = 'ind',
                         label = u"Plus-values non commerciaux professionnels de cession taxables à 16% (régime de la déclaration controlée, revenus bénéficiant de l'abattement association agrée ou viseur)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5QD",
                                        QUIFOY['conj']: u"5RD",
                                        QUIFOY['pac1']: u"5SD", })),  # (f5qd, f5rd, f5sd)),

    build_column_couple('nbnc_pvce', IntCol(entity = 'ind',
                         label = u"Déficits industriels et commerciaux: locations meublées sans CGA (régime du bénéfice réel)",
                         val_type = "monetary",
                         cerfa_field = {QUIFOY['vous']: u"5QJ",
                                        QUIFOY['conj']: u"5RJ",
                                        QUIFOY['pac1']: u"5SJ", })),  # (f5qj, f5rj, f5sj)),

    ))

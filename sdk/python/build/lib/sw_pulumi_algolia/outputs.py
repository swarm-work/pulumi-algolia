# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetIndexSettingResult',
]

@pulumi.output_type
class GetIndexSettingResult(dict):
    def __init__(__self__, *,
                 advanced_syntax: bool,
                 advanced_syntax_features: Sequence[str],
                 allow_compression_of_integer_array: bool,
                 allow_typos_on_numeric_tokens: bool,
                 alternatives_as_exacts: Sequence[str],
                 attribute_criteria_computed_by_min_proximity: bool,
                 attribute_for_distinct: str,
                 attributes_for_facetings: Sequence[str],
                 attributes_to_highlights: Sequence[str],
                 attributes_to_retrieves: Sequence[str],
                 attributes_to_snippets: Sequence[str],
                 camel_case_attributes: Sequence[str],
                 custom_rankings: Sequence[str],
                 disable_exact_on_attributes: Sequence[str],
                 disable_prefix_on_attributes: Sequence[str],
                 disable_typo_tolerance_on_attributes: Sequence[str],
                 disable_typo_tolerance_on_words: Sequence[str],
                 distinct: int,
                 enable_personalization: bool,
                 enable_rules: bool,
                 exact_on_single_word_query: str,
                 hits_per_page: int,
                 index_languages: Sequence[str],
                 max_facet_hits: int,
                 max_values_per_facet: int,
                 min_proximity: int,
                 min_word_sizefor1_typo: int,
                 min_word_sizefor2_typos: int,
                 numeric_attributes_for_filterings: Sequence[str],
                 optional_words: Sequence[str],
                 pagination_limited_to: int,
                 primary: str,
                 query_languages: Sequence[str],
                 query_type: str,
                 rankings: Sequence[str],
                 remove_words_if_no_results: str,
                 replace_synonyms_in_highlight: bool,
                 replicas: Sequence[str],
                 restrict_highlight_and_snippet_arrays: bool,
                 searchable_attributes: Sequence[str],
                 separators_to_index: str,
                 snippet_ellipsis_text: str,
                 sort_facet_values_by: str,
                 unretrievable_attributes: Sequence[str]):
        pulumi.set(__self__, "advanced_syntax", advanced_syntax)
        pulumi.set(__self__, "advanced_syntax_features", advanced_syntax_features)
        pulumi.set(__self__, "allow_compression_of_integer_array", allow_compression_of_integer_array)
        pulumi.set(__self__, "allow_typos_on_numeric_tokens", allow_typos_on_numeric_tokens)
        pulumi.set(__self__, "alternatives_as_exacts", alternatives_as_exacts)
        pulumi.set(__self__, "attribute_criteria_computed_by_min_proximity", attribute_criteria_computed_by_min_proximity)
        pulumi.set(__self__, "attribute_for_distinct", attribute_for_distinct)
        pulumi.set(__self__, "attributes_for_facetings", attributes_for_facetings)
        pulumi.set(__self__, "attributes_to_highlights", attributes_to_highlights)
        pulumi.set(__self__, "attributes_to_retrieves", attributes_to_retrieves)
        pulumi.set(__self__, "attributes_to_snippets", attributes_to_snippets)
        pulumi.set(__self__, "camel_case_attributes", camel_case_attributes)
        pulumi.set(__self__, "custom_rankings", custom_rankings)
        pulumi.set(__self__, "disable_exact_on_attributes", disable_exact_on_attributes)
        pulumi.set(__self__, "disable_prefix_on_attributes", disable_prefix_on_attributes)
        pulumi.set(__self__, "disable_typo_tolerance_on_attributes", disable_typo_tolerance_on_attributes)
        pulumi.set(__self__, "disable_typo_tolerance_on_words", disable_typo_tolerance_on_words)
        pulumi.set(__self__, "distinct", distinct)
        pulumi.set(__self__, "enable_personalization", enable_personalization)
        pulumi.set(__self__, "enable_rules", enable_rules)
        pulumi.set(__self__, "exact_on_single_word_query", exact_on_single_word_query)
        pulumi.set(__self__, "hits_per_page", hits_per_page)
        pulumi.set(__self__, "index_languages", index_languages)
        pulumi.set(__self__, "max_facet_hits", max_facet_hits)
        pulumi.set(__self__, "max_values_per_facet", max_values_per_facet)
        pulumi.set(__self__, "min_proximity", min_proximity)
        pulumi.set(__self__, "min_word_sizefor1_typo", min_word_sizefor1_typo)
        pulumi.set(__self__, "min_word_sizefor2_typos", min_word_sizefor2_typos)
        pulumi.set(__self__, "numeric_attributes_for_filterings", numeric_attributes_for_filterings)
        pulumi.set(__self__, "optional_words", optional_words)
        pulumi.set(__self__, "pagination_limited_to", pagination_limited_to)
        pulumi.set(__self__, "primary", primary)
        pulumi.set(__self__, "query_languages", query_languages)
        pulumi.set(__self__, "query_type", query_type)
        pulumi.set(__self__, "rankings", rankings)
        pulumi.set(__self__, "remove_words_if_no_results", remove_words_if_no_results)
        pulumi.set(__self__, "replace_synonyms_in_highlight", replace_synonyms_in_highlight)
        pulumi.set(__self__, "replicas", replicas)
        pulumi.set(__self__, "restrict_highlight_and_snippet_arrays", restrict_highlight_and_snippet_arrays)
        pulumi.set(__self__, "searchable_attributes", searchable_attributes)
        pulumi.set(__self__, "separators_to_index", separators_to_index)
        pulumi.set(__self__, "snippet_ellipsis_text", snippet_ellipsis_text)
        pulumi.set(__self__, "sort_facet_values_by", sort_facet_values_by)
        pulumi.set(__self__, "unretrievable_attributes", unretrievable_attributes)

    @property
    @pulumi.getter(name="advancedSyntax")
    def advanced_syntax(self) -> bool:
        return pulumi.get(self, "advanced_syntax")

    @property
    @pulumi.getter(name="advancedSyntaxFeatures")
    def advanced_syntax_features(self) -> Sequence[str]:
        return pulumi.get(self, "advanced_syntax_features")

    @property
    @pulumi.getter(name="allowCompressionOfIntegerArray")
    def allow_compression_of_integer_array(self) -> bool:
        return pulumi.get(self, "allow_compression_of_integer_array")

    @property
    @pulumi.getter(name="allowTyposOnNumericTokens")
    def allow_typos_on_numeric_tokens(self) -> bool:
        return pulumi.get(self, "allow_typos_on_numeric_tokens")

    @property
    @pulumi.getter(name="alternativesAsExacts")
    def alternatives_as_exacts(self) -> Sequence[str]:
        return pulumi.get(self, "alternatives_as_exacts")

    @property
    @pulumi.getter(name="attributeCriteriaComputedByMinProximity")
    def attribute_criteria_computed_by_min_proximity(self) -> bool:
        return pulumi.get(self, "attribute_criteria_computed_by_min_proximity")

    @property
    @pulumi.getter(name="attributeForDistinct")
    def attribute_for_distinct(self) -> str:
        return pulumi.get(self, "attribute_for_distinct")

    @property
    @pulumi.getter(name="attributesForFacetings")
    def attributes_for_facetings(self) -> Sequence[str]:
        return pulumi.get(self, "attributes_for_facetings")

    @property
    @pulumi.getter(name="attributesToHighlights")
    def attributes_to_highlights(self) -> Sequence[str]:
        return pulumi.get(self, "attributes_to_highlights")

    @property
    @pulumi.getter(name="attributesToRetrieves")
    def attributes_to_retrieves(self) -> Sequence[str]:
        return pulumi.get(self, "attributes_to_retrieves")

    @property
    @pulumi.getter(name="attributesToSnippets")
    def attributes_to_snippets(self) -> Sequence[str]:
        return pulumi.get(self, "attributes_to_snippets")

    @property
    @pulumi.getter(name="camelCaseAttributes")
    def camel_case_attributes(self) -> Sequence[str]:
        return pulumi.get(self, "camel_case_attributes")

    @property
    @pulumi.getter(name="customRankings")
    def custom_rankings(self) -> Sequence[str]:
        return pulumi.get(self, "custom_rankings")

    @property
    @pulumi.getter(name="disableExactOnAttributes")
    def disable_exact_on_attributes(self) -> Sequence[str]:
        return pulumi.get(self, "disable_exact_on_attributes")

    @property
    @pulumi.getter(name="disablePrefixOnAttributes")
    def disable_prefix_on_attributes(self) -> Sequence[str]:
        return pulumi.get(self, "disable_prefix_on_attributes")

    @property
    @pulumi.getter(name="disableTypoToleranceOnAttributes")
    def disable_typo_tolerance_on_attributes(self) -> Sequence[str]:
        return pulumi.get(self, "disable_typo_tolerance_on_attributes")

    @property
    @pulumi.getter(name="disableTypoToleranceOnWords")
    def disable_typo_tolerance_on_words(self) -> Sequence[str]:
        return pulumi.get(self, "disable_typo_tolerance_on_words")

    @property
    @pulumi.getter
    def distinct(self) -> int:
        return pulumi.get(self, "distinct")

    @property
    @pulumi.getter(name="enablePersonalization")
    def enable_personalization(self) -> bool:
        return pulumi.get(self, "enable_personalization")

    @property
    @pulumi.getter(name="enableRules")
    def enable_rules(self) -> bool:
        return pulumi.get(self, "enable_rules")

    @property
    @pulumi.getter(name="exactOnSingleWordQuery")
    def exact_on_single_word_query(self) -> str:
        return pulumi.get(self, "exact_on_single_word_query")

    @property
    @pulumi.getter(name="hitsPerPage")
    def hits_per_page(self) -> int:
        return pulumi.get(self, "hits_per_page")

    @property
    @pulumi.getter(name="indexLanguages")
    def index_languages(self) -> Sequence[str]:
        return pulumi.get(self, "index_languages")

    @property
    @pulumi.getter(name="maxFacetHits")
    def max_facet_hits(self) -> int:
        return pulumi.get(self, "max_facet_hits")

    @property
    @pulumi.getter(name="maxValuesPerFacet")
    def max_values_per_facet(self) -> int:
        return pulumi.get(self, "max_values_per_facet")

    @property
    @pulumi.getter(name="minProximity")
    def min_proximity(self) -> int:
        return pulumi.get(self, "min_proximity")

    @property
    @pulumi.getter(name="minWordSizefor1Typo")
    def min_word_sizefor1_typo(self) -> int:
        return pulumi.get(self, "min_word_sizefor1_typo")

    @property
    @pulumi.getter(name="minWordSizefor2Typos")
    def min_word_sizefor2_typos(self) -> int:
        return pulumi.get(self, "min_word_sizefor2_typos")

    @property
    @pulumi.getter(name="numericAttributesForFilterings")
    def numeric_attributes_for_filterings(self) -> Sequence[str]:
        return pulumi.get(self, "numeric_attributes_for_filterings")

    @property
    @pulumi.getter(name="optionalWords")
    def optional_words(self) -> Sequence[str]:
        return pulumi.get(self, "optional_words")

    @property
    @pulumi.getter(name="paginationLimitedTo")
    def pagination_limited_to(self) -> int:
        return pulumi.get(self, "pagination_limited_to")

    @property
    @pulumi.getter
    def primary(self) -> str:
        return pulumi.get(self, "primary")

    @property
    @pulumi.getter(name="queryLanguages")
    def query_languages(self) -> Sequence[str]:
        return pulumi.get(self, "query_languages")

    @property
    @pulumi.getter(name="queryType")
    def query_type(self) -> str:
        return pulumi.get(self, "query_type")

    @property
    @pulumi.getter
    def rankings(self) -> Sequence[str]:
        return pulumi.get(self, "rankings")

    @property
    @pulumi.getter(name="removeWordsIfNoResults")
    def remove_words_if_no_results(self) -> str:
        return pulumi.get(self, "remove_words_if_no_results")

    @property
    @pulumi.getter(name="replaceSynonymsInHighlight")
    def replace_synonyms_in_highlight(self) -> bool:
        return pulumi.get(self, "replace_synonyms_in_highlight")

    @property
    @pulumi.getter
    def replicas(self) -> Sequence[str]:
        return pulumi.get(self, "replicas")

    @property
    @pulumi.getter(name="restrictHighlightAndSnippetArrays")
    def restrict_highlight_and_snippet_arrays(self) -> bool:
        return pulumi.get(self, "restrict_highlight_and_snippet_arrays")

    @property
    @pulumi.getter(name="searchableAttributes")
    def searchable_attributes(self) -> Sequence[str]:
        return pulumi.get(self, "searchable_attributes")

    @property
    @pulumi.getter(name="separatorsToIndex")
    def separators_to_index(self) -> str:
        return pulumi.get(self, "separators_to_index")

    @property
    @pulumi.getter(name="snippetEllipsisText")
    def snippet_ellipsis_text(self) -> str:
        return pulumi.get(self, "snippet_ellipsis_text")

    @property
    @pulumi.getter(name="sortFacetValuesBy")
    def sort_facet_values_by(self) -> str:
        return pulumi.get(self, "sort_facet_values_by")

    @property
    @pulumi.getter(name="unretrievableAttributes")
    def unretrievable_attributes(self) -> Sequence[str]:
        return pulumi.get(self, "unretrievable_attributes")



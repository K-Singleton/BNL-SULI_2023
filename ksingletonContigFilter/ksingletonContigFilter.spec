/*
A KBase module: ksingletonContigFilter
This sample module contains one small method that filters contigs.
*/

module ksingletonContigFilter {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_ksingletonContigFilter(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;
    /*
        New app which filters contigs in an assembly using both a minimum and a maximum contig length
    */
  funcdef run_ksingletonContigFilter_max(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
